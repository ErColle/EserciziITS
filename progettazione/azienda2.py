from custom_types import RealGEZ
import datetime

class Impiegati: 
    _nome: str 
    _cognome: str
    _nascita: datetime.date
    _stipendio: RealGEZ
    
    def nome(self):
        return self._nome
    
    def cognome(self):
        return self._cognome
    
    def nascita(self):
        return self._nascita
    
    def stipendio(self):
        return self._stipendio
    
   # setters
   
    def set_nome(self, nome: str):
        self._nome = nome
        
    def set_cognome(self, cognome: str):
        self._cognome = cognome
