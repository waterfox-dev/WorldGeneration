from source.tools.load_biomes import load_biomes
from source.classes.world import World

from source.utils.show import show


biomes = load_biomes()
w = World('test', 100, biomes, False)
w.set_biomes_center(5)
w.fill_world()
w.write('assets/output.json')
w.load('assets/output.json')
show(w)