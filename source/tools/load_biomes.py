import json 

from source.hintings import Biome

def load_biomes(preset_file="data/preset.json") -> list[Biome] : 
    """Open a preset file and load it content as biomes preset.

    Args:
        preset_file (str, optional): The location of the preset file, a `.json` is require.Defaults to "data/preset.json".

    Returns:
        dict[dict]: a dict where key are biomes and value descriptions.
    """
    
    biomes = list()
    
    with open(preset_file, 'r', encoding='utf8') as preset :
        
        preset = dict(json.load(preset))
        
        for key in preset.keys() :
            biomes.append(preset[key])
        
        return biomes