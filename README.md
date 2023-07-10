# World Generation - V2



**World generation is a little project in python who the objectif is to generate a world
with a simple preset.
The generation is volontary "*simple*" and is the fruit of simples maths rules.**

## Generate a world 

The first step is to implement a preset file, a preset file is a `.json`. The structure is :
```json
//Preset.json 
{
    "biomeCode" :
    {
        "name" : "biomeName",
        "code" : "biomeCode", 
        "color": "biomeColor", 
        "weight" : "biomeWeight" // The weight define the influence of your biome
    }
}
```
*A complete exemple :  [here](assets/output.json)*

Now, you can create a world with preset file :
```py
from source.tools.load_biomes import load_biomes
from source.classes.world import World

biomes = load_biomes('assets/output.json')
w = World('name', 100, biomes, False)
```

To generate a world you need to set biomes center :
```py
w.set_biomes_center(5) #Number of biome center
```

And, you can fill it :
```py
w.fill_world() 
```
## Show a World 
If you want to have a visual representation of your world, you can use the
show function : `source.utils.show`. It loads a world and generate a graphic version into the folder `assets/output.png`.
```py
from source.utils.show import show
show(w)
```

