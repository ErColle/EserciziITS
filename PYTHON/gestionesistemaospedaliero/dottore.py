from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specializzazione: str, parcella: float):
        super().__init__(first_name, last_name)
        
        if isinstance(specializzazione, str):
            self.__specializzazione = specializzazione
            
        else:
            self.__specializzazione = None
            print("La specializzazione inserita non è una stringa!")
            
        if isinstance(parcella, float):
            self.__parcella = parcella
        else: 
            self.__parcella = None 
            print("La parcella inserita non è un float")
            
    def setParcel(self, parcella):
        
        if isinstance(parcella, float):
            self.__parcella = parcella
        else:
            raise ValueError("La parcella inserita non è un float!")
        
    def setSpecialization(self, specializzazione):
        
        if isinstance(specializzazione, str):
            self.__specializzazione = specializzazione
        else:
            raise ValueError("La specializzazione inserita non è una stringa!")
        
    def getParcel(self):
        return self.__parcella
    
    def getSpecialization(self):
        return self.__specializzazione
    
    def isAValidDoctor(self):
        if self.getAge() > 30:
            return f"Doctor {self.getName()} {self.getLastName()} is valid"
        else: 
            return f"Doctor {self.getName()} {self.getLastName()} is not valid"
        
    def doctorGreet(self):
        self.greet()
        return f"Sono un medico {self.getSpecialization()}"
    
dottore = Dottore("Luca", "Rossi", "Chirurgo", 3.1)
dottore.setAge(45)
print(dottore.doctorGreet())
print(dottore.isAValidDoctor())
            
        
        