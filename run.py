from source.classes.world import World 
from source.tools.load_biomes import load_biomes
from source.utils.show import show

import os 
import sys


if int(sys.version.split('.')[1]) > 0 and int(sys.version.split('.')[0]) > 2 :
    args = list(sys.argv[1:])
    if(len(args) != 4) :
        raise TypeError("Too many or not enought arguments")
    else :
        biomes = load_biomes(args[2])
        world = World(args[0], int(args[1]), biomes)
        world.set_biomes_center(int(args[3]))
        world.fill_world()
        show(world)

else :
    raise OSError('Python must version must be >= 3.10')