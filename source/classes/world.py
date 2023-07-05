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
    
    
    def _weight_to_force(self, biome: Biome) -> int :
        return round(biome['weight'] * self.size / 100, 0)

    def _get_influences(self, pos: tuple[int]) -> dict[Biome:int] :
        
        influences = {}
        
        for center_pos in self.biomes_center :
            
            cell:Cell = self.grid[center_pos[0]][center_pos[1]]
            distance = abs(center_pos[0] - pos[0]) + abs(center_pos[1] - pos[1])
            
            if cell.biome['code'] not in list(influences.keys()) :
                influences[cell.biome['code']] = []
            
            influences[cell.biome['code']].append(distance) 
        
        
        for key, value in influences.items() : 
            influences[key] = sum(value)/len(value)
        
        return influences   
            
    def set_biomes_center(self, nb_biome: int) -> list[tuple[int]] :
        """Set biomes center on the grid.

        Args:
            nb_biome (int): Number of biome.
        
        Returns:
            list[tuple[int]]: list of biome center as a tuple (x,y)
        """
        
        self.biomes_center = []
        
        for i in range(nb_biome):
            
            pos_x = random.randint(0,self.size - 1)
            pos_y = random.randint(0, self.size - 1)
            biome = random.choice(self.biomes)
            
            self.grid[pos_x][pos_y] = Cell(biome)
            self.biomes_center.append((pos_x, pos_y))
        
        return self.biomes_center
    
    def fill_world(self) -> None :
        
        for i in range(len(self.grid)) :
            for j in range(len(self.grid[i])) :
                if((i, j) not in self.biomes_center) :
                    max_key = [key for key, value in self._get_influences((i,j)).items() if value == min(self._get_influences((i,j)).values())]
                    for k in range(len(self.biomes)) :
                        if self.biomes[k]['code'] == max_key[0] :
                            self.grid[i][j] = Cell(self.biomes[k])
            
