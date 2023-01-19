from source.world import World
from source.utils import display_as_img

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

w = World(preset, 100).generate()
display_as_img(w)