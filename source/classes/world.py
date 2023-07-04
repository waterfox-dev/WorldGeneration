import logging
import random

from source.classes.cell import Cell
from source.hintings import Biome


class World :
    
    def __init__(self, name: str, size: int, biome_list: list[Biome]) -> None :
        """Create an instance of a world. A world is composed of mutliple Cell. 

        Args:
            name (str): The name of the world
            size (int): The size of the world. A world is a square of `size` dimensions
            biome_list (dict): The list of biomes possible in this world
        """
        self.name = name 
        self.size = size
        self.biomes = biome_list
        self.grid:list[list[Cell]] = list()        
        
        for i in range(size) :
            self.grid.append(list())
            for j in range(size) :
                self.grid[i].append(None)
                
    def __str__(self) -> str :
        
        content = ""
        
        for c in range(len(self.grid)) :
            for l in range(len(self.grid)) :
                if self.grid[c][l] == None :
                    content += ' NG '
                else :
                    content += f" {self.grid[c][l].biome['code']} "
            content += '\n'
    
        return content
    
    def set_biomes_center(self, nb_biome: int) -> None :
        """Set biomes center on the grid.

        Args:
            nb_biome (int): Number of biome.
        """
        for i in range(nb_biome):
            pos_x = random.randint(0,self.size - 1)
            pos_y = random.randint(0, self.size - 1)
            biome = random.choice(self.biomes)
            self.grid[pos_x][pos_y] = Cell(biome)