from dottore import Dottore 
from paziente import Paziente

class Fattura:
    
    def __init__(self, patient: list, doctor):
        
        if doctor.isAValidDoctor(doctor):
            self.__fatture = len(patient)
            self.__salary = 0 
        else: 
            self.__patient = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
            
    def getSalary(self):
        
        self.__salary = self.doctor.getParcel() * self.fatture
        return self.__salary
    
    def getFatture(self):
        
        self.__fatture = len(self.__patient)
        return self.__fatture
        
            
            
        