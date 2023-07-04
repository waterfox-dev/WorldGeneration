# World Generation - V1


***Warning : If you want to run V1, switch to branch `V1-Stable`***


****World generation** is a little project in python who the objectif is to generate a world
with a simple preset.
The generation is volontary "*simple*" and is the fruit of simples maths rules.**

## Generate a world

To generate a world you need two things :

- A **preset** : This is python dict who define the generation preset
- A **size**: This is the size of your world, it's a square

### Config a preset

A preset is a python `dict`, it's like :

```python
preset = { 
    0 : {  #The preset for biome '0' :
        0 : 40, # - probabilty of a biome '0' near 40%
        1 : 60, # - probabilty of a biome '0' near 60%    
    }, 
    1 : {
        0 : 60, 
        1 : 40, 
    }
}
```

A preset can got as much as you want biome, **but**, each biome dict need to have each biome key, and the sum of each value need to be 100.

### Generate a world

A world is a `list` who the struct is `list[int]`, wich in represents a biome's id.
To generate a world you can :

```python
from source.world import World

w = World(preset, 5)
print(w.generate())
```

**Version** : Generator v.1
=======================

# World Generation

**World generation** is a little project in python who the objectif is to generate a world
with a simple preset.
The generation is volontary "*simple*" and is the fruit of simples maths rules.

## Generate a world

To generate a world you need two things :

- A **preset** : This is python dict who define the generation preset
- A **size**: This is the size of your world, it's a square

### Config a preset

A preset is a python `dict`, it's like :

```python
preset = { 
    0 : {  #The preset for biome '0' :
        0 : 40, # - probabilty of a biome '0' near 40%
        1 : 60, # - probabilty of a biome '0' near 60%    
    }, 
    1 : {
        0 : 60, 
        1 : 40, 
    }
}
```

A preset can got as much as you want biome, **but**, each biome dict need to have each biome key, and the sum of each value need to be 100.

### Generate a world

A world is a `list` who the struct is `list[int]`, wich in represents a biome's id.
To generate a world you can :

```python
from source.world import World

w = World(preset, 5)
print(w.generate())
```

>>>>>>> origin/interface
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>
