import random

class Creatura:
    
    def __init__(self, nome: str):
        
        self.setNome(nome)
        
    def setNome(self, nome):
        
        if isinstance(nome, str):
            self._nome = nome
        
        else: 
            self._nome = "Creatura Generica"
    
    def getNome(self):
        return self._nome
    
    def __str__(self):
        return f"Nome creatura: {self._nome}\n"
    

class Alieno(Creatura):
    
    def __init__(self, nome):
        
        super().__init__(nome)
        self._setMatricola()
        self._setMunizioni()
        
        if nome != f"Robot-{self._matricola}":
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!')
            
            self._nome = f"Robot-{self._matricola}"
            
        else: 
            self._nome = f"Robot-{self._matricola}"
                   
    def _setMatricola(self):
        self._matricola = random.randint(10000, 90000)

    def _setMunizioni(self):
        self._munizioni = [i * i for i in range(15)] 
        
    def getMunizioni(self):
        return self._munizioni
    
    def getMatricola(self):
        return self._matricola
    
    def getNome(self):
        return self._nome

    def __str__(self):
        return f"Alieno: {self._nome}\n"
    

class Mostro(Creatura): 
    
    def __init__(self, nome, urlo_di_vittoria: str, gemito_di_sconfitta: str):
        
        super().__init__(nome)
        self._urlo_di_vittoria = urlo_di_vittoria
        self._gemito_di_sconfitta = gemito_di_sconfitta
        self._setAssalto()
        
    def _setAssalto(self):
        self._assalto = random.sample(range(1, 101), 15)
    
    def getAssalto(self): 
        return self._assalto
    
    def setVittoria(self):
        
        if self._urlo_di_vittoria != "GRAAAHHH":
            print("Urlo vittoria erratto! ")
            self._urlo_di_vittoria = "GRAAAHHH"
            
        else:
            self._gemito_di_sconfitta = "GRAAAHHH"
            
    def setSconfitta(self):
        
        if self._urlo_di_vittoria != "Uuurghhh":
            print("Gemito sconfitta erratto! ")
            self._gemito_di_sconfitta = "Uuurghhh"
            
        else:
            self._gemito_di_sconfitta = "Uuurghhh"
            
    def getVittoria(self):
        return self._urlo_di_vittoria
    
    def getSconfitta(self):
        return self._gemito_di_sconfitta
        
            
    def __str__(self):

        nome_cambiato = ""
        
        for i, lettera in enumerate(self._nome):
            if i % 2 == 0:
                nome_cambiato += lettera.upper()
            else:
                nome_cambiato += lettera.lower()
                
        return f"Mostro: {nome_cambiato}\n"
    
            
def pariUguali(a: list[int], b: list[int]) -> list[int]:
    
    c = []
    
    for i in range(min(len(a), len(b))):
        
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
            
        else:
            c.append(0)
    return c

def combattimento(a: Alieno, m: Mostro):
    
    if isinstance(a, Alieno) and isinstance(m, Mostro):
        
        ris = pariUguali(a.getMunizioni(), m.getAssalto())
        
        if ris.count(1) == 4:
            print(f"{m.getVittoria()}\n{m.getVittoria()}\n{m.getVittoria()}")
            return m
        
        else:
            print(f"{m.getSconfitta()}\n")
            return a
    
    else: 
        print("Cobattimento interrotto!")
        return None
    
""" proclamaVincitore(c: Creatura). 
Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri ( a seconda dell'oggetto c) e , 
mostra il vincitore all'interno di un rettangolo con contorno di * come nell'esempio. """

def proclamaVincitore(c: Creatura):
    if isinstance(c, Alieno):
        print(f"Hanno vinto gli ALIENI\n{c.getNome()}")
    elif isinstance(c, Mostro):
        print(f"Hanno vinto i MOSTRI\n{c.getNome()}")
    
mostro1 = Mostro("Mostro", "aaaaa", "bbbbb")
mostro1.setVittoria()
mostro1.setSconfitta()
print(mostro1.getVittoria())
print(mostro1.getSconfitta())
print(mostro1)
    
alieno1 = Alieno("Robot")
print(alieno1.getMatricola())
print(alieno1.getMunizioni())
print(alieno1.getNome())
print(alieno1)
    
   
creatura1 = Creatura("Luca")
creatura1.setNome(123)
creatura1.setNome("Luca")
print(creatura1.getNome())
print(creatura1)


vincitore = combattimento(alieno1, mostro1)
if vincitore:
    proclamaVincitore(vincitore)


    
    