import numpy as np
from math import floor

# iso module

tile_width,tile_height = 64,64
i = np.array([1 * (tile_width/2), 0.5 * (tile_height/2)]) 
j = np.array([-1 * (tile_width/2),0.5 * (tile_height/2)]) 

determinant = ((i[0]*j[1])-(j[0]*i[1]))
transpose = np.array([j[1], -j[0], -i[1], i[0]])
inv_matrix = (1/determinant) * transpose
print(inv_matrix)

"""
tile_width,tile_height = 0,0
i = np.empty([2])
j = np.empty([2])
determinant = 0
transpose = np.empty([4])
inv_matrix = np.empty([4])

"""

"""
def iso_initialize(width, height):
    tile_width, tile_height = width, height
    create_transform_matrice(tile_width, tile_height)

def create_transform_matrice(width,heigh):
    i = np.array([1 * (width/2), 0.5 * (heigh/2)]) 
    j = np.array([-1 * (width/2),0.5 * (heigh/2)]) 

    determinant = ((i[0]*j[1])-(j[0]*i[1]))
    transpose = np.array([j[1], -j[0], -i[1], i[0]])
    inv_matrix = (1/determinant) * transpose
    print(inv_matrix)
"""


def tile_coordinate_to_screen(x,y):

    x_screen_coord = x * i[0] + y * j[0] 
    y_screen_coord = x * i[1] + y * j[1]
    
    return x_screen_coord, y_screen_coord

def screen_to_tile_coordinate(x,y):

    x_tile_coord = x * inv_matrix[0] + y  * inv_matrix[1]
    y_tile_coord = x * inv_matrix[2] + y * inv_matrix[3]
    
    return floor(x_tile_coord), floor(y_tile_coord)