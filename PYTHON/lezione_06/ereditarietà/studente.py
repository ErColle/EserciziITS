#importare dal modulo persona.py la classe Persona
from PYTHON.lezione_06.ereditarietà.persona import Persona

class Studente(Persona):
    '''
    Attributi classe persona
    self.name: str 
    self.lastname: str
    self.age: int
    
    Attributi della classe Studenti
    self.matricola: str
    
    '''
    
#inizializzare un oggetto della classe Studente

def __init__(self, name:str, lastname:str, age:int, matricola:str):
    
    
    # iniziallizzare  la classe Persona richiamando il metodo init dellla supeclasse.  
    super().__init__(name, lastname, age)
    
    # istruzioni che inizializzano un oggetto della classe Studente
    self.setMatricola(matricola)
    
#metodi setter

#metodo che imposta valore dell'attributo self.matricola
def setMatricola(self, matricola: str):
    if matricola:
        self.matricola = matricola 
    else: 
        print("Errore! la matricola non può essere  rappresentata da una stringa vuota")
        
#metodi getter 

#metodo che ritorna il valore dell'attributo self.matricola
def getMatricola:



  

