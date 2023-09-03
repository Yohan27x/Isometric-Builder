import tweener
from iso_functions import tile_coordinate_to_screen,screen_to_tile_coordinate
from helper_functions import load_img
from tweener import *


class IsoTile:
    def __init__(self, x_tile, y_tile, z_pos, img, height, duration, tile_type="tile", reset=False):

        self.type = tile_type
        self.height = height
        
        self.x_coord = x_tile
        self.y_coord = y_tile
        self.z_coord = z_pos

        self.remove = False

        self.img = img

        self.x_screen, self.y_screen = tile_coordinate_to_screen(self.x_coord - self.z_coord, self.y_coord - self.z_coord)

        self.duration = duration
        self.tween_started = False

        # if reset == False:

        #     self.tween = Tween(begin=height, 
        #         end = self.y_screen,
        #         duration=self.duration,
        #         easing=Easing.CIRC,
        #         easing_mode=EasingMode.IN_OUT,
        #         boomerang=False, 
        #         loop=False)
        # else:
        self.tween = Tween(begin=height, 
                end = self.y_screen,
                duration=self.duration,
                easing=Easing.CUBIC,
                easing_mode=EasingMode.OUT,
                boomerang=False, 
                loop=False)
        

    def get_easing(self):
        easing = str(self.tween._easing)
        mode = str(self.tween._easing_mode)

        return easing + mode

    def change_coordinate(self,x,y):

        self.x_coord = x
        self.y_coord = y 
        
        # self.tween._begin = self.y_screen
        # self.tween_started = False
    
        self.x_screen, self.y_screen = tile_coordinate_to_screen(self.x_coord - self.z_coord, self.y_coord - self.z_coord)

        # -- tween --
        # self.tween._end += self.img.get_width()

    def is_removed(self, duration):
        self.remove = True
        # print("self.y_screen :", self.y_screen)
        self.tween = Tween(begin=self.y_screen, 
            end = self.height,
            duration=duration,
            easing=Easing.QUAD,
            easing_mode=EasingMode.IN,
            boomerang=False, 
            loop=False)
        
       
       
        

        
        

        

