from dottore import Dottore, dottore
from paziente import paziente1, paziente2, paziente3

class Fattura(Dottore):
    
    def __init__(self, pazienti: list, dottore: str):
        self.__pazienti = list(pazienti)
        self.__dottore = dottore
        if self.isAValidDoctor() == True:
            self.__fatture = len(self.__pazienti)
            self.__salary = 0
        else:
            self.__fatture = None 
            self.__salary = None 
            self.__pazienti = None 
            self.__dottore = None
    def getSalary(self):
        self.__salary = self.getParcel() * self.__fatture
        return self.__salary
    
    def getFatture(self):
        self.__fatture = len(self.__pazienti)
        return self.__fatture
    def addPatient(self, newPatient: str):
        self.__pazienti.append(newPatient)
        self.getFatture()
        self.getSalary()
        self.getSalary
        
    def removePatient(self, idCode: str):
        for paziente in self.__pazienti:
            if paziente.getIdCode() == idCode:
                self.__pazienti.remove(paziente)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {self.__dottore} è stato rimosso il paziente {idCode}.")
                break
            
pazienti = [paziente1, paziente2, paziente3]
fattura = Fattura(pazienti, dottore)


    
        
            
            
        