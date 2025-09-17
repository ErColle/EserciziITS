class Persona:
    
    def __init__(self, first_name:str, last_name:str):
        
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è  una stringa!")
            
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")
            
        if isinstance(first_name, str) and isinstance(last_name, str):
            self.__age = 0
        else:
            self.__age = None
    
    def SetName(self, first_name: str):
        
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            raise ValueError("Il nome insierito non è una stringa!")
        
    def setLastName(self, last_name: str):
        
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            raise ValueError("Il nome insierito non è una stringa!")
        
    def setAge(self, age:int):
        
        if isinstance(age, int):
            self.__age = age
        
        else:
            raise ValueError("L'età inserita non è un numero intero!")
    
    def getName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age    
    
    def greet(self):
        return f"Ciao sono {self.getName()} {self.getLastName()}! Ho {self.getAge()}"
        
persona = Persona("Luca", "Rossi")
persona.setAge(15)
print(persona.getAge())
print(persona.greet())
