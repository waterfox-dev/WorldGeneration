from typing import TypedDict 

class Biome(TypedDict) :
    """Represend a TypedDict who is a biome
    """
    name: str 
    code: str
    color: str
    weight: int