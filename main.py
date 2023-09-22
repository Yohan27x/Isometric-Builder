import pygame, sys, os, random, math, tweener, time
from mss import mss
import mss.tools
from itertools import zip_longest
from pygame.locals import *
import numpy as np
from numpy.linalg import inv
from math import floor
from tweener import *
from helper_functions import load_img
#from iso_functions import iso_initialize, tile_coordinate_to_screen,screen_to_tile_coordinate
from iso_functions import tile_coordinate_to_screen,screen_to_tile_coordinate
from IsoTile import IsoTile


# ---------- NEXT -----------
# - add to github
# - 
# - random tile or let the user choose his own tile, for color reasons
# - add a music and fx -> Reaper 
# - it's too static, add movement : random wave, up - down with idk ... Whats the feeling you want the user to feel ? 
# - 

# ---------- DONE ---------------
# -OK :  add "on top" placement to place tile on mouse loc -> ie two ways of placing tile, one at the mouse loc ( the most trivial), and one to place it behind ( you cant to it with the first one )
# - OK : make the map moove ? sin wave ? 
# - OK : add remove tile, use tween. Control Z or remove tile by clicking ? ctrl z seems to be a better option, both programming and designing 
# - add tile preview, can be turn on and off
# --------- Pygame settings ----------------------

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)

pygame.display.set_caption('Pygame Window')
os.environ['SDL_VIDEODRIVER'] = 'directx'

flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED

font = pygame.font.Font("font/8-BIT WONDER.TTF")

WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT), flags, vsync=True)

clock = pygame.time.Clock()
timer = pygame.time.Clock()

#-------- ISO Variables ---------------------------------------------

SCALE = 4
num_available_tiles = 4
available_tiles = []
select_tile_index = 0
tile_width = 0
tile_height = 0

for index in range(num_available_tiles):
    path = "tile_" + str(index) + ".png"
    tile_img = load_img(path,SCALE)
    tile_width = tile_img.get_width() 
    tile_height = tile_img.get_height()
    available_tiles.append(tile_img)

print(available_tiles)
print("tile size ", tile_width, "/", tile_height)
select_tile = available_tiles[select_tile_index]
mouse_hover_tile_img = load_img("new_hover.png", SCALE)
grid = load_img("grid.png", SCALE)
# grid_tile_img = load_img("grid_tile.png", SCALE)

ordered_tiles = []
non_ordered_tiles = []

OFFSET = (WIDTH/2, HEIGHT/2.8)
SCROLL_Y_OFFSET = 0
SCROLL_X_OFFSET = 0
print("OFFSET : ", OFFSET)

TWEEN_DURATION = 850
tiles_anim_finished = False
tile_preview = False

show_grid = False
select_on_front = False
random_mode = True
reset_map = False

scroll_direction = [False,False,False,False]

mouse_tile = IsoTile(0, 0, 0, mouse_hover_tile_img, 0, 2000 , "mouse")

def reset_tiles(columns=10, rows=10, random_percent=0):
    ordered_tiles.clear()
    removed_tiles.clear()
    for y in range(columns):
        for x in range(rows):
                if random.random() > random_percent:
                    tile = IsoTile(x,y,1,available_tiles[random.randrange(0,4)], HEIGHT, 3300, "tile", True)
                    ordered_tiles.append(tile)

    ordered_tiles.append(mouse_tile)

    # for index in range(140):
    #     tile = IsoTile(random.randrange(0,15),random.randrange(0,15),0,available_tiles[random.randrange(0,4)], HEIGHT, TWEEN_DURATION)
    #     tiles.append(tile)

    sort_tiles()

def sort_tiles():

    ordered_tiles.sort(key=lambda tile: (tile.z_coord, tile.x_coord, tile.y_coord), reverse=False)

    # for i,tile in enumerate(ordered_tiles):
    #     print("tile ", i)
    #     print("z : ", tile.z_coord)
    #     print("x : ", tile.x_coord)
    #     print("y : ", tile.y_coord)
       
    
def add_tile(x,y):
    highest_z = 1

    for tile in ordered_tiles:
        if highest_z < tile.z_coord:
            highest_z = tile.z_coord

    # print("highest_z : ", highest_z)

    platforms = []
    for z_index in range(highest_z):
        platforms.append([])

    # print("platforms : ", platforms)

    # split the tiles in their respective z platform
    for i,platform in enumerate(platforms):
        for tile in ordered_tiles:
            if(tile.z_coord == i + 1):
                platforms[i].append(tile)

    z_tile_to_add = 1

    for i,platform in enumerate(platforms):
        for tile in platform:
            if tile.x_coord == x and tile.y_coord == y and tile.type == "tile":
                # print("in")
                z_tile_to_add = tile.z_coord + 1

    # print("z_tile_to_add : ", z_tile_to_add)

    tile_to_add = IsoTile(x, y, z_tile_to_add, select_tile, HEIGHT - SCROLL_Y_OFFSET, TWEEN_DURATION + 50)
    ordered_tiles.append(tile_to_add)
    non_ordered_tiles.append(tile_to_add)

    # mouse_tile.tween_started = False


removed_tiles = []
def remove_last_tile():
    if(len(non_ordered_tiles) != 0):
        last_added_tile = non_ordered_tiles.pop(len(non_ordered_tiles)-1)
        if last_added_tile.tween._animating == False:
            last_added_tile.is_removed(TWEEN_DURATION )
            last_added_tile.tween.start()
            # removed_tiles.append(last_added_tile)
            # ordered_tiles.remove(last_added_tile)


reset_tiles(5,5)
non_ordered_tiles = ordered_tiles.copy()
non_ordered_tiles.pop(0)

while True :

    screen.fill((0,0,0))

    # ---------- UI -------------

    if(show_grid == True):
        screen.blit(grid, (-8,-102))
        
    osciliation = (math.sin(pygame.time.get_ticks()/1000)) * 5
    osciliation = 0

    num_of_tiles_UI = font.render(str(len(ordered_tiles)-1),  True, (240,178,0))
    screen.blit(num_of_tiles_UI,(20,20))

    if(select_on_front == True):
        blit_style = "Behind"
    else:
        blit_style = "Top"

    select_behind_text_UI = font.render(blit_style, True, (240,178,0))
    screen.blit(select_behind_text_UI,(558,20))
    
    select_tile = available_tiles[select_tile_index]
    screen.blit(pygame.transform.scale(select_tile,(tile_width/2, tile_height/2)), (20, 56))

    # --------- COORDINATE -------------------

    pos = pygame.mouse.get_pos()

    x_screen_mouse = pos[0] - OFFSET[0]
    y_screen_mouse = pos[1] - OFFSET[1]  
    x_tile_mouse, y_tile_mouse = screen_to_tile_coordinate(x_screen_mouse, y_screen_mouse)

    if(select_on_front == False):
        x_tile_mouse += 1
        y_tile_mouse += 1
        
    highest_z = 0
    for tile in ordered_tiles:
        if(tile.type == "tile" and tile.x_coord == x_tile_mouse and tile.y_coord == y_tile_mouse):
            highest_z = tile.z_coord

    mouse_tile.z_coord = highest_z
    mouse_tile.z_coord += 1
    mouse_tile.change_coordinate(x_tile_mouse ,y_tile_mouse)

    sort_tiles()

    if tile_preview:
        mouse_tile.img = select_tile
    else:
        mouse_tile.img = mouse_hover_tile_img

    # ---------------- TILES --------------

    # Trigger animation one time for all tiles

    for tile in ordered_tiles:
        if(tile.tween_started == False):#tile.type == "tile" and 
            #screen.blit(tile_img,(tile.x_screen - tile_width/2 + OFFSET[0] , tile.y_screen + OFFSET[1]))
            tile.tween_started = True
            tile.tween.start()

    # Blit all the tiles
    tiles_anim_finished = True
    for tile in ordered_tiles.copy():
        tile.tween.update()
        if(tile.type == "tile"):
            screen.blit(tile.img,(tile.x_screen - tile_width/2 + OFFSET[0] + SCROLL_X_OFFSET , tile.tween.value + OFFSET[1] + SCROLL_Y_OFFSET))
        else:
            screen.blit(tile.img,(tile.x_screen - tile_width/2 + OFFSET[0] , tile.y_screen + OFFSET[1] ))
        
        if(tile.tween._animating == True):
            tiles_anim_finished = False

        if(tile.remove == True and tile.tween._animating == False):
            ordered_tiles.remove(tile)

    if reset_map and tiles_anim_finished:
        reset_tiles(random.randrange(0,9),random.randrange(0,9), random.random() - 0.9)
        reset_map = False
    # -------------------- INPUT ------------------------------------

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
               pygame.quit()
               sys.exit()

            if event.key == K_i:
                show_grid = not show_grid

            if event.key == K_k:
                select_on_front = not select_on_front

            if event.key == K_o:
                tile_preview = not tile_preview

            if event.key == K_z:
                remove_last_tile()

            if event.key == K_m:
                if(tiles_anim_finished == True):
                    for tile in ordered_tiles:
                        tile.tween._begin = tile.tween._end
                        tile.tween._easing = Easing.BACK
                        tile.tween._easing_mode = EasingMode.IN_OUT
                        tile.tween._duration = TWEEN_DURATION + 1900
                        tile.tween._end = HEIGHT
                        tile.tween.start()
                    reset_map = True

            if event.key == K_LEFT:
                SCROLL_X_OFFSET -= tile_width 

            if event.key == K_RIGHT:
                SCROLL_X_OFFSET += tile_width

            if event.key == K_UP:
                SCROLL_Y_OFFSET += tile_width / 2

            if event.key == K_DOWN:
                SCROLL_Y_OFFSET -= tile_width / 2

        if event.type == KEYUP:
            if event.key == K_o:
                for tile in ordered_tiles:
                    tile.tween.resume()



        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                # print("x_tile_mouse : ", x_tile_mouse)
                # print("SCROLL_Y_OFFSET/(tile_width / 2 : ", SCROLL_Y_OFFSET/(tile_width / 2))
                # print(" SCROLL_X_OFFSET/(tile_width / 2)", SCROLL_X_OFFSET/(tile_width / 2))
                # print(x_tile_mouse, y_tile_mouse)
                if(random_mode == True):
                    select_tile_index = random.randrange(0,4)
               
                add_tile(x_tile_mouse - SCROLL_Y_OFFSET/(tile_width / 2), y_tile_mouse - SCROLL_Y_OFFSET/(tile_width / 2))
                sort_tiles()

            # if event.button == 4:
            #     select_tile_index += 1
            #     if(select_tile_index == len(available_tiles)):
            #         select_tile_index = 0


    pygame.display.update()
    clock.tick(60)
   