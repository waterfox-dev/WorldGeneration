from source.tools.load_biomes import load_biomes
from source.classes.world import World


biomes = load_biomes()
w = World('test', 20, biomes)
w.set_biomes_center(2)
print(w)