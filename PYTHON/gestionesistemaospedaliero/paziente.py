from persona import Persona 

class Paziente(Persona):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        
    def setidCode(self, idCode: str):
        
        self.__idCode = idCode
        
    def getIdCode(self):
        return self.__idCode
    
    def PatientInfo(self):
        return f"Paziente:{self.getName()} {self.getLastName()}\nID:{self.__idCode}"
    
paziente1 = Paziente("Luca", "Rossi")
paziente1.setidCode("ciaociao")

paziente2 = Paziente("Francesco", "Rossi")
paziente2.setidCode("yoyoyoyoyyo")

paziente3 = Paziente("Martina", "Rossi")
paziente3.setidCode("wewewewe")

print(paziente1.PatientInfo())