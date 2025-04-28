from esempiopersona import Persona
from alieno import Alieno

#creare un oggetto della classe Persona 
p: Persona = Persona('Luca', 'Rossi', 29)

print(p)

#creare un oggetto della classe Persona 
et: Alieno = Alieno("Andromeda")

print(et)

#invocare il metodo speak() della classe Persona
p.speak()

#invocare il metodo speak() della classe Alieno
et.speak()



