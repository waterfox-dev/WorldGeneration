from source.world import World 

import logging

class Generator : 
    
    def __init__(self, preset: dict[int, dict[int, int]], dim: int, biome_range: int, log=False) -> None: 
        
        self.preset = preset 
        self.dim = dim
        self.biome_range = biome_range
        self.log = log
    
    def generate(self,  world_occurence: int) -> list[list[int]]:
                
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S %p', level=logging.INFO)
        
        gen = World(self.preset, self.dim).generate(self.biome_range)
        
        for i in range(world_occurence): 
            if self.log :
                logging.info(f"Generating World {i+1}...")
            temp = World(self.preset, self.dim)
            temp.import_world(gen)
            gen = temp.generate(self.biome_range)
            if self.log : 
                logging.info("Done !")
        
        return gen
            