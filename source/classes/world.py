import logging
import random
import json

from source.classes.cell import Cell
from source.hintings import Biome

class World :
    
    def __init__(self, name: str, size: int, biome_list: list[Biome], log:bool = False) -> None :
        """Create an instance of a world. A world is composed of mutliple Cell. 

        Args:
            name (str): The name of the world.
            size (int): The size of the world. A world is a square of `size` dimensions
            biome_list (dict): The list of biomes possible in this world
            log (bool, optional): The log state. Defaults to False.
        """
        self.name = name 
        self.size = size
        self.biomes = biome_list
        self.log = log 
    
        self.grid:list[list[Cell]] = list()   
        self.pos = [(i,j) for i in range(size) for j in range(size)]     
        
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
    
        if self.log :
            print(f"Influences of {pos}")
            
        influences = {}
        
        for center_pos in self.biomes_center :
            
            cell:Cell = self.grid[center_pos[0]][center_pos[1]]
            distance = abs(center_pos[0] - pos[0]) + abs(center_pos[1] - pos[1])
            
            if cell.biome['code'] not in list(influences.keys()) :
                influences[cell.biome['code']] = []
            
            influences[cell.biome['code']].append(distance/self._weight_to_force(cell.biome)) 
            
            if self.log :
                print(f"[{cell.biome['name']} : {distance/self._weight_to_force(cell.biome)}]")
        
        for key, value in influences.items() : 
            influences[key] = sum(value)/len(value)
        
        return influences   
    
    def _code_to_biome(self, code : str) -> Biome :
        
        for biome in self.biomes :
            if biome['code'] == code :
                return biome
            
    def _grid_to_json(self) -> list[list[str]] :
        
        out:list[list[str]] = list()
        
        for i in range(self.size) : 
            out.append(list())
            for j in range(self.size) :
                out[i].append(self.grid[i][j].biome['code'])
        
        return out
    
    def _json_to_grid(self, data : list[list[str]]) -> list[list[Cell]] :
        
        out:list[list[Cell]] = list()
        
        for i in range(self.size) : 
            out.append(list())
            for j in range(self.size) :
                out[i].append(Cell(self._code_to_biome(data[i][j])))
                        
        return out
        
        
                
    def set_biomes_center(self, nb_biome: int) -> list[tuple[int]] :
        """Set biomes center on the grid.

        Args:
            nb_biome (int): Number of biome.
        
        Returns:
            list[tuple[int]]: list of biome center as a tuple (x,y)
        """
        
        if self.log :
            print("=== Generating Biomes Center ===")
        
        self.biomes_center = []
        
        for i in range(nb_biome):
            
            pos_x = random.randint(0,self.size - 1)
            pos_y = random.randint(0, self.size - 1)
            biome = random.choice(self.biomes)
            
            self.grid[pos_x][pos_y] = Cell(biome)
            print((pos_x, pos_y))
            self.pos.remove((pos_x, pos_y))
            self.biomes_center.append((pos_x, pos_y))
            
            if self.log :            
                print(f"({pos_x},{pos_y}) - {biome['name']}")
        
        return self.biomes_center
    
    def fill_world(self) -> None :
        """Fill the current world with generated Cell
        """
        
        if self.log :
            print("=== Generating Cell ===")
        
        while self.pos != [] :
            pos = random.choice(self.pos)
            self.pos.remove(pos)
            max_key = [key for key, value in self._get_influences(pos).items() if value == min(self._get_influences(pos).values())]
            for k in range(len(self.biomes)) :
                if self.biomes[k]['code'] == max_key[0] :
                    
                    self.grid[pos[0]][pos[1]] = Cell(self.biomes[k])

                    if self.log :
                        print(f"-> {self.biomes[k]['name']}")
    
    def write(self, filepath:str) -> None :
        """Write a `.json` with the world settings 

        Args:
            filepath (str): the filepath of the save
        """
        
        with open(filepath, 'w', encoding='utf8') as f_write :
            datas = {}
            datas['biomes'] = self.biomes
            datas['world'] = self._grid_to_json()
            json.dump(datas, f_write)

    def load(self, filepath: str) :
        
        with open(filepath, 'r', encoding='utf8') as f_read :
            datas = json.load(f_read)
            self.biomes = datas['biomes']
            self.grid = self._json_to_grid(datas['world'])