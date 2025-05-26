import re
from datetime import *
    
class Indirizzo:
    # l'underscore indica attributi protetti, possono accedere anche le sottoclassi di indirizzo
    _via: str
    _civico: int

    def _init_(self, via: str, civico: int) -> None:

        self._via = via
        self._civico = civico

    def via(self):

        return self._via
    
    def civico(self):

        return self._civico
    

    def _hash_(self):
        # l'hash si calcola con i campi dell'init
        return hash( (self._via, self._civico) )
    
    def _eq_(self, other) -> bool:

        if  other is None or  not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return self._via == other._via and self._civico == other._civico
    
class Telefono(str):

    def _new_(cls, telefono: str):

        pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
        # pattern migliorato ^\+?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{4,6}$
        if re.match(pattern, telefono):

            return str._new_(cls, telefono)
        
        else:

            raise ValueError('Inserire un numero di telefono valido')
        
class RealGEZ(float):

    def _new_(cls, num: int | float):

        if num > 0:

            return super()._new_(cls, num)
        
        raise ValueError(f'Il numero {num} deve essere un numero maggiore di zero')
    



class Impiegato:

    _nome: str
    _cognome: str
    _nascita: datetime.date
    _stipendio: RealGEZ


    def _init_(self, nome: str, cognome: str, nascita: datetime.date, stipendio: RealGEZ ):

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    
    def get_nome(self) -> str:

        return self._nome
    
    def set_nome(self, new_name: str) -> None:

        self._nome = new_name

    def get_cognome(self) -> str:

        return self._cognome
    
    def set_cognome(self, new_cognome: str) -> None:

        self._cognome = new_cognome

    def get_nascita(self) -> datetime.date:

        return self._nascita
    
    
    def get_stipendio(self) -> RealGEZ:

        return self._stipendio
    
    def set_stipendio(self, new_stipendio: RealGEZ) -> None:

        self._stipendio = new_stipendio

        
class Dipartimento:

    _nome: str
    _telefono: set[Telefono]
    _indirizzo: Indirizzo

    def _init_(self, nome: str, telefono: Telefono):

        self.set_nome(nome)
        self.add_telefono(telefono)
        self._indirizzo = None

    def get_nome(self) -> str:

        return self._nome
    
    def set_nome(self, new_name: str) -> None:

        self._nome = new_name

    def get_telefono(self) -> frozenset[Telefono]:

        return self._telefono
    
    def add_telefono(self, new_telefono: Telefono) -> None:

        self._telefono.add(new_telefono)

    
    def remove_telefono(self, t: Telefono) -> None:

        if len(self.telefono()) > 1:

            self._telefono.remove(t)

        raise RuntimeError('Uno studente deve avere minimo un numero')
    
    def get_indirizzo(self) -> Indirizzo:

        return self._indirizzo
    
    def set_indirizzo(self, new_indirizzo: Indirizzo) -> None:

        self._indirizzo = new_indirizzo

class Progetto:

    _nome: str
    _budget: RealGEZ

    def _init_(self, nome: str, budget: RealGEZ):
        
        self.set_nome(nome)
        self.set_budget(budget)

    def get_nome(self) -> str:

        return self._nome
    
    def set_nome(self, new_nome: str) -> None:

        self._nome = new_nome
    
    def get_budget(self) -> RealGEZ:

        return self._budget
        
    def set_budget(self, new_budget: RealGEZ) -> None:

        self._budget = new_budget               