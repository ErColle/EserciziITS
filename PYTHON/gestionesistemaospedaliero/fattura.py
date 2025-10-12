from dottore import Dottore 
from paziente import Paziente

class Fattura:
    
    def __init__(self, patients: list, doctor):
        
        if doctor.isAValidDoctor(doctor):
            self.__fatture = len(patients)
            self.__salary = 0 
        else: 
            self.__patients = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
            
    def getSalary(self):
        
        self.__salary = self.doctor.getParcel() * self.fatture
        return self.__salary
    
    def getFatture(self):
        
        self.__fatture = len(self.__patients)
        return self.__fatture
    
    def addPatient(self, newPatient):
        self.__patients.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato aggiunto il paziente {newPatient.getidCode()}")
        
    def removePatient(self, idCode: str):

        if self.patients is not None:
            for p in self.patients:
                if p.getidCode() == idCode:
                    self.patients.remove(p)
                    self.getFatture()   
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato rimosso il paziente {idCode}")

                print(f"Nessun paziente trovato con ID {idCode}")        
            
            
        