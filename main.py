<<<<<<< HEAD
from source.generator import Generator 
from source.utils import display_as_img

import logging

preset = { 
    0 : {  
        0 : 33,
        1 : 33,
        2 : 33,
    }, 
    1 : {
        0 : 33, 
        1 : 33,
        2 : 33, 
    },
    2 : {
        0 : 33, 
        1 : 33, 
        2 : 33 
    }
}

render = Generator(preset, 10, 4, True).generate(1)
display_as_img(render)
=======
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
>>>>>>> origin/interface
