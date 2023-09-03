# helper functions file
import pygame

def load_img(path,scale = 1,colorkey=(255,255,255)):

    type = path.split("/")[-1]
    type = type.split(".")[-1]

    if type == "png":
        img = pygame.image.load(path).convert_alpha()
    else:
        img = pygame.image.load(path).convert()

    img.set_colorkey(colorkey)

    new_width = img.get_width() * scale
    new_height = img.get_height() * scale
    img = pygame.transform.scale(img, (new_width, new_height))

    return img
