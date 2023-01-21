from typing import TypedDict
from ipythonblocks import BlockGrid, colors

import matplotlib.pyplot as plt
import matplotlib.image as img



def print_dict(d: dict) -> None:
    for key, value in d.items():
        print(f"{key} : {value}")
    
        
def display_world(world: list[list[int]]) -> None:
    
    grid = BlockGrid(width=len(world), height=len(world[0]), fill=colors['WhiteSmoke'], block_size=30)
    
    for x in range(len(world)):
        for y in range(len(world[x])):
            if world[x][y] == 1: 
                grid[x, y].set_colors(0,0,0)
                
            if world[x][y] == 2: 
                grid[x, y].set_colors(0,150,64)
   
    grid.show()

def display_as_img(world: list[list[int]]) -> None: 
    
    grid = BlockGrid(width=len(world), height=len(world[0]), fill=colors['WhiteSmoke'], block_size=30)
    
    for x in range(len(world)):
        for y in range(len(world[x])):
            if world[x][y] == 1: 
                grid[x, y].set_colors(111,215,48)
                
            if world[x][y] == 2: 
                grid[x, y].set_colors(250,128,114)  
    
    grid.save_image('assets/generation.png')
    im = img.imread('assets/generation.png')
    plt.imshow(im)
    plt.show()