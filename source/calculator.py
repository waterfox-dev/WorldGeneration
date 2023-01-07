def get_close(world: list[list[int]], posset: set, pos: tuple[int], cell_type: int) -> set:
        
    for x in range(pos[0]-1, pos[0]+2):
        if x == -1 or x == pos[0] or x >= len(world[0]):
            pass
        else : 
            if world[x][pos[1]] == cell_type  and (x,pos[1]) not in posset: 
                posset.add((x,pos[1]))
                
    for y in range(pos[1]-1, pos[1]+2):
        if y == -1 or y == pos[1] or y >= len(world[0]):
            pass 
        else : 
            if world[pos[0]][y] == cell_type and (pos[0],y) not in posset:
                posset.add((pos[0],y))     
                
    return posset

def get_biome_size(world: list[list[int]], biome_id: int) -> tuple[set, int] : 
    
    posset = set()
    
    for line in range(len(world)):
        for column in range(len(world)): 
            get_close(world, posset, (line, column), biome_id)  
    
    return posset, len(posset)
