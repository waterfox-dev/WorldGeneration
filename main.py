from source.tools.load_biomes import load_biomes
from source.classes.world import World

from source.utils.show import show


biomes = load_biomes()
w = World('test', 100, biomes)
w.set_biomes_center(12)
w.fill_world()
show(w)

