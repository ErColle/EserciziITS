from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from azienda.impiegato import Impiegato
    from azienda.progetto import Progetto

class coinvolto: 
    
    _impiegato: 'Impiegato'    #ovviamente immutabile, noto alla nascita 
    _progetto: 'Progetto'      #ovviamente immutabile, noto alla nascita 
    _data: date                #immutabile, noto alla nascita 
    

    def __init__(self, impiegato: Impiegato, progetto: Progetto, data: date)-> None:
        self._impiegato = impiegato
        self._progetto = progetto
        self._data = data 
        
    def impiegato(self):
        return self._impiegato
    
    def progetto(self):
        return self._progetto
    
    def data(self):
        return self._data
    
    def __hash__(self):
        return hash((self.impiegato(), self.progetto()))
    
    def __eq__(self, other):
        if 