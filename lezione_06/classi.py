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

#ATTRIBUTI DI CLASSE 

class Student:
    
    studentGrades = []  #--> ATTRUBUTO DI CLASSE 
    
    def __init__(self, studentName, grade):
        
        self.name = studentName
        self.studentGrades.append(grade)
        
    def getGroupAverage(cls):
        avg = sum(cls.studentGrades) / len(cls.studentGrades)#--> cls SERVE PER ACCEDERE ATTRIBUTI DI CLASSE (equivalente self) 
        return avg
    
#MEDOTO STR -> SERVE PER RAPPRESENTARE UNA CLASSE IN STRINGA
#SE NON VIENE DEFINITO, OUTPUT STAMPA LA POSIZIONE IN MEMORIA DELLA CLASSE

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __str__(self):
        return f"{self.nome} ha {self.eta} anni"
    
p = Persona("Alice", 25)
print(str(p))   # Alice ha 25 anni

#METODO CALL -> SERVE PER RENDERE UN OGGETTO "CALLABLE" (COME UNA FUNZIONE)

class Saluta:
    def __init__(self, nome):
        self.nome = nome

    def __call__(self):
        return f"Ciao, {self.nome}!"

s = Saluta("Alice")
print(s())  # Output: Ciao, Alice!






  