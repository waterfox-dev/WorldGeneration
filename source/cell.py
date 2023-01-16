class Cell : 
    
    def __init__(self, pos: tuple, biome: int) -> None: 
        self.pos = pos 
        self.biome = biome
        self.influences = []
    
    def __repr__(self) -> str:
        return f'[{self.pos[0]},{self.pos[1]}]'