from source.hintings import Biome


class Cell :
    
    def __init__(self, biome_type: Biome) -> None :
        """Create an instance of a cell.

        Args:
            biome_type (dict): a biome dictionnary from the preset file 
        """
        self.biome = biome_type
        
    def __str__(self) -> str :
        return self.biome['name']