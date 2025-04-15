class Persona: 

    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = ""
    
    def displayData(self):
        
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age} ")
        
       
   # mi consente di impostare un valore per self.name     
    def setName( self, name:str ):
        
        self.name = name
        
   # mi consente di impostare un valore per self.lastname    
    def setLastname( self, lastname:str ):
        
        self.lastname = lastname


# mi consente di impostare un valore per self.age
    def setAge( self, age:int ):
        
        if age < 0 or age > 120:
            self.age = 0
        else: 
            self.age = age
            
            
# restituisce valore di name
    def GetName(self):
        
        return self.name

# restituisce valore di lastname
    def GetLastname(self):
        
        return self.lastname
    
# restituisce valore di age   
    def GetAge(self):
    
        return self.age
        


# crea oggetto di tipo persona
f:Persona = Persona()

# impostare il nome di una persona 
f.setName("Alessandro")

# impostare il cognome di una persona
f.setLastname("Colella")

#impostare l'età di una persona
f.setAge(20)


# stampa i dati della persona creata
f.displayData()

# stampo utilizzando il metodo get
print(f.GetName(), f.GetLastname(), f.GetAge())