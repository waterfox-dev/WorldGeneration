import pickle 

def save(world: list, filename: str) -> None :
    
    with open(f'assets/gen/{filename}', 'wb') as file : 
        pickle.dump(world, file)
        
def load(filename: str) -> list : 
    
    with open(f'assets/gen/{filename}', 'rb') as file : 
        w = pickle.load(file)
    
    return w