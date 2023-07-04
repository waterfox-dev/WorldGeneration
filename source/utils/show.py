import matplotlib.pyplot as plt

from matplotlib import colors
from ipythonblocks import BlockGrid

from source.classes.world import World

def _hexa_to_rgb(hexa: str) -> tuple[int] : 
    hexa = hexa.lstrip('#')
    return tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))

def show(world: World) -> None :
    
    grid = BlockGrid(world.size, world.size, fill=(255,255,255), lines_on=False)
    print(grid.height)
    
    for c in range(len(world.grid)-1) :
        for l in range(len(world.grid)-1) :
            if world.grid[c][l] != None :
                print(c, l)
                grid[c,l].rgb = (_hexa_to_rgb(world.grid[c][l].biome['color']))
    
    grid.save_image('test.png')
    