from persona import Persona
from studente import Studente

#creo un oggetto della classe persona 
fm: Persona = Persona("Alessandro", "Colella", 20)

#visuallizzare  le informazioni relaive all'oggetto fm
print(fm)

#creo un oggetto della classe Studente
studente1: Studente = Studente("Mario", "Rossi", 20, "")

#visuallizzare le informazioni relative all'oggetto  studente1 
print(studente1)

#controllo se studente1 sia instanza della classe Studente
# inistance(obj, class) --> controlla se l'oggetto obj sia un'instanza della classe Class
# in caso affermativo -> True 
# in caso negativo -> False

if isinstance(studente1, Studente):
    print("\nstudente1 è un istanza della classe Studente ")
    
if isinstance(studente1, Persona):
    print("\nstudente1 è anche un istanza della classe Persona")
    
#controllare se l'oggetto fm sia istanza della classe persona
if isinstance(fm, Persona):
    print("\n l'oggetto fm è un istanza della classe Persona")
    
#Controllare se l'oggetto fm è un istanza della classe Studente

if isinstance(fm, Studente):
    print("\nl'oggetto fm è un istanza della classe Studente")

else: 
    print("\nl'oggetto fm è un istanza della classe Persona ma non è istanza della classe Studente")
    
# controllare che se la classe Studente sia sottoclasse della classe Persona
# issubclass(Class1, Class2)-> controlla se Class1 sia sottoclasse della classe Class2
# in caso affermativo -> True
# in caso negativo -> False

if issubclass(Studente, Persona):
    print("\n la classe Studente è sottoclasse della classe Persona")


    



