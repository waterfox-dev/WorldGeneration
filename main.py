from source.tools.load_biomes import load_biomes
from source.classes.world import World

from source.utils.show import show


biomes = load_biomes()
w = World('test', 200, biomes)
w.set_biomes_center(10)
w.fill_world()
show(w)