#LE CLASSI 

#DEFINIRE CLASSE 

class Person():
    
    def __init__(self, name, age): #METODO COSTRUTTORE 
        self.name = name
        self.age = age


persona1 = Person("Luca", 20) #ISTANZA 
persona2 = Person("Mattia", 15)

persona2.name = "Carlo"

print(persona2.age) #STAMPA ATTRUBUTO AGE 
print(persona2.name) #STAMPA ATTRIBUTO NAME 

#SELF
# - SELF PERMETTE L'ACCESSO E LA MODIFICA DEI DATI DELL'OGGETTO
# - COLLLEGA GLI ATTRIBUTI AI METODI DELLA CLASSE  

class Persona():
    
    def __init__(self, nome, cognome):
        self.nome = nome 
        self.cognome = cognome
    
    def saluta(self): #SELF RAPPRESENTA PERSONA  
        
        print(f"Ciao! sono {self.nome} ")
    
persona3 = Persona("Luca", "Verdi")

persona3.saluta() #RICHIAMO METODO SALUTA 


  