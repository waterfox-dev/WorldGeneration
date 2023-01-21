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