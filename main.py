from source.world import World
from source.utils import display_as_img

preset = { 
    0 : {  #The preset for biome '0' :
        0 : 50, # - probabilty of a biome '0' near 40%
        1 : 50, # - probabilty of a biome '0' near 60%      
    }, 
    1 : {
        0 : 10, 
        1 : 90, 
    }
}

w = World(preset, 10).generate(8)
display_as_img(w)