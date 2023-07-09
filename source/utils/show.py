import matplotlib.pyplot as plt

from matplotlib import colors
from ipythonblocks import BlockGrid

from source.classes.world import World

def _hexa_to_rgb(hexa: str) -> tuple[int] : 
    hexa = hexa.lstrip('#')
    return tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))

def show(world: World) -> None :
    """Save world as png image into `assets/output.png`.

    Args:
        world (World): the world to generate
    """
    grid = BlockGrid(world.size, world.size, fill=(100,100,100), lines_on=False, block_size=5)
    
    for c in range(len(world.grid)) :
        for l in range(len(world.grid)) :
            if world.grid[c][l] != None :
                grid[c,l].rgb = (_hexa_to_rgb(world.grid[c][l].biome['color']))
    
    grid.save_image('assets/output.png')
    