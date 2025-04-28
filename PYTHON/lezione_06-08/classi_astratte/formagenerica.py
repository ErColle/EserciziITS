from abc import ABC, abstractmethod


class FormaGenerica(ABC): 
    
    @abstractmethod 
    def draw(self):
        pass
    
    def setShape(self, shape:str):
        if shape: 
            self.shape = shape
        else: 
            print("shape non puo essere un stringa vuota")
    
    def getShape(self):
        return self.shape
