from source.world import World
from source.utils import display_as_img
from source.loader import load, save


preset = { 
    0 : {  #The preset for biome '0' :
        0 : 40, # - probabilty of a biome '0' near 40%
        1 : 60, # - probabilty of a biome '0' near 60%      
    }, 
    1 : {
        0 : 60, 
        1 : 40, 
    }
}

gen = World(preset, 30).generate(5)

for i in range(30) : 
    print("Step :", i+1)
    w = World(preset, 30)
    w.import_world(gen)
    gen = w.generate(30)

display_as_img(gen)