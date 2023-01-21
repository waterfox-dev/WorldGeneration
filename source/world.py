from ipythonblocks import BlockGrid, colors

from source.cell import Cell

import random


class World :
    
    def __init__(self, preset: dict, size: int) -> None:
        
        self._l_world : list[list[Cell]]
        
        self._l_world = list()
        self.size = size
        self.preset = preset
        
        for x in range(size): 
            self._l_world.append([])
            for y in range(size):
                self._l_world[x].append(Cell((x,y), 0)) #Todo : Not 0 but None
        
    def _analyse_neighbor(self, pos: tuple[int], biome_range: int) -> None :
        
        self._l_world[pos[0]][pos[1]].influences = list()
        
        for x in range(pos[0]-biome_range, pos[0]+biome_range+1):
            for y in range(pos[1]-biome_range, pos[1]+biome_range+1) :
                if ((x,y) == pos) or ((x or y) <= -1) or (y >= (len(self._l_world[0]) - 1)) or ((x >= (len(self._l_world[0]) - 1))):
                    pass 
                else :
                    self._l_world[pos[0]][pos[1]].influences.append(self._l_world[x][y].biome)
        
    def _set_biome(self, pos: tuple[int]) -> None :
        
        l_prob = list()
        
        for element in self._l_world[pos[0]][pos[1]].influences :
            
            rm_list = []
            for biome, prob in self.preset[element].items() :
                rm_list.extend([biome]*prob)
            
            l_prob.append(random.choice(rm_list))
            
        self._l_world[pos[0]][pos[1]].biome = int(round(sum(l_prob)/len(l_prob), 0))
    
    def generate(self, biome_range: int) -> list:
        
        for x in range(len(self._l_world)) :
            for y in range(len(self._l_world)) :
                self._analyse_neighbor((x,y), biome_range)
                self._set_biome((x,y))
 
        l = list()
        
        for x in range(len(self._l_world)):
            l.append([])
            for y in range(len(self._l_world)):
                l[x].append(self._l_world[x][y].biome)

        return l
    
    def import_world(self, world: list[list[int]]) -> None:
        
        for x in range(len(world)) :
            for y in range(len(world[0])): 
                self._l_world[x][y] = Cell((x,y), world[x][y])
    
    def __repr__(self) -> str:
        
        total = str()
        
        for x in range(len(self._l_world)) : 
            line = str()            
            for y in range(len(self._l_world[0])) :
                line += str(self._l_world[x][y].biome)
            
            total += line + '\n'
        return total
