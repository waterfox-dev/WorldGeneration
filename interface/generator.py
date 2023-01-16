import tkinter as tk 

class MainWindow :
    
    def __init__(self) -> None : 
        
        self.win = tk.Tk()
        self.win.geometry("960x540")
        self.win.title("World Generator")
        
    def show(self) -> None :
        self.win.mainloop()
        
        