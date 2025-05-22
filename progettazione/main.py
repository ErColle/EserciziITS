import re 
from typing import Self

#CREO TIPI DI DATO CHE IN PYTHON NON ESISTONO

class CodiceFiscale(str): #super classe str 
    # gli oggetti di questa classe sono stringe che rispettano il formato del codice fiscale
    
    
    def __new__(cls, cf: str): #costruttore della classe che crea un nuovo oggetto di tipo CodiceFiscale
        
        cff: str = cf.upper().strip() #rendo la stringa maiuscola e tolgo gli spazi
        
        if re.fullmatch(r'[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]', cff):
            
            return super().__new__(cls, cff) #crea un nuovo oggetto di tipo str con il valore cff 
        else:
            raise ValueError('Inserire un codice fiscale valido')


""" class CodiceFiscale: # classe che rappresenta un codice fiscale (maniera brutta)


   # gli oggetti di questa contengono una stringa che rispetta il formato del codice fiscale 
   
   cf: str
   def __init__(self, cf: str):
       
       cff: str = cf.upper().strip() #rendo la stringa maiuscola e tolgo gli spazi
        
       # inizializza l'oggetto con il codice fiscale
       if re.fullmatch(r'[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]', cf):
           
           self.cf = cff
           
       else: 
           raise ValueError('Inserire un codice fiscale valido') """
           
class CAP(str): #super classe str 
    # gli oggetti di questa classe sono stringe che rispettano il formato del codice fiscale
    
    
    def __new__(cls, cap: str): #costruttore della classe che crea un nuovo oggetto di tipo CodiceFiscale
        
        
        if re.fullmatch(r'\d{5}', cap):
            
            return super().__new__(cls, cap) #crea un nuovo oggetto di tipo str con il valore cff 
        else:
            raise ValueError('Inserire un CAP valido')

class RealGEZ(float): #super classe float 
    # tipo di dato specializzato Reale >= 0
    
    def __new__(cls, valore: float|int|bool|Self):
        valore: float = float.__new__(cls, valore) # prova a convertire il valore in float
        
        if valore > 0: 
            return valore
        else: 
            raise  ValueError('Il valore deve essere maggiore di 0')
        
class Valuta(str):
    def __new__(cls, valuta: str):
        if re.fullmatch(r'[A-Z]{3}', valuta):
            return super().__new__(cls, valuta)
        else:
            raise ValueError('Inserire una valuta valida')

class Denaro: 
   # rappresenta il tipo di dato concettuale composto con i seguenti campi:
   # - importo: RealGEZ
   # - valuta: Valuta
   _importo: float
   _valuta: float
   
   def __init__(self, importo: float, valuta: Valuta):
       # inizializza l'oggetto con i valori importo e valuta
       self._importo = importo
       self._valuta = valuta
       
       def importo(self):
           # restituisce l'importo
           return self._importo
       
       def valuta(self):
           # restituisce la valuta
           return self._valuta
       
       def __str__(self):
           return f"{self._importo()} {self._valuta()}"
       
       def __repr__(self): 
           return f'Denaro({self._importo()}, {self._valuta()})'
       
       def __hash__(self):
           return hash((self._importo, self._valuta))
       
       def __eq__(self, other):
           
           if not isinstance(other, type(self)) or \
                hash(self) != hash(other):
                return False
           else: 
                return self._importo == other._importo and \
                self.valuta() == other.valuta() 
          

denaro = Denaro(5.0, Valuta('EUR')) # crea un oggetto di tipo Denaro con importo 5.0 e valuta EUR

print(denaro) # stampa l'oggetto Denaro

x = RealGEZ(5.0) # crea un oggetto di tipo RealGEZ con valore 5.0 (reale > 0)
""" y = RealGEZ(-5.0) # crea un oggetto di tipo RealGEZ con valore -5.0 """

cf1 = CodiceFiscale('RSSMRA85M01H501Z') #codice fiscale1 
           