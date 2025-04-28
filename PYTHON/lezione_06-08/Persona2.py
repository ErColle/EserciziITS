class Persona:
    
    '''
    
    Di un persona dobbiamo sapere delle informazioni.
    Queste informazioni viengono chiamate  attributi (della classe Persona
    Le informazioni saranno :
     
    - nome 
    -cognome 
    - età
    
    come li rappresento in Python?
    
    self.name:str
    
    self.lastname:str
    
    self.age:int
    '''

   # costruttore classe persona 
   
    def __init__(  self, name:str , lastname:str, age:int ): 
        
        self.name  = name 
        self.lastname = lastname
        self.age = age
        
       #funzione che mostra in output tutti i dati di una persona  
    
    def displayData(self):
        
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age} ")
        
#Mostra dati di un persona

f:Persona = Persona("Alessandro", "Colella", 20)

f.displayData()






