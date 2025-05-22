from enum import *
import re
class Indirizzo:
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
        return hash( (self._via, self._civico) )
    
    def _eq_(self, other) -> bool:

        if  other is None or  not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return self._via == other._via and self._civico == other._civico
    


class StatoOrdine(StrEnum):

    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class CodiceFiscale():

    def _init_(self, cf):
        
        self.cf = self.cf_validation(cf)

    def cf_validation(self, cf: str) -> str:

        pattern = r'[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}'
        cf = cf.upper()
        if re.match(pattern, cf):

            return cf
        else:

            raise ValueError('Inserire un codice fiscale valido')
        
    def _eq_(self, other) -> bool:
        
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):

            return False
        return(self.cf) == (other.cf)
    
    def _hash_(self):
        return hash(self.cf)
    

class PartitaIva(str):

    def _new_(cls, iva: str):

        patten = r'\d{11}'

        if re.match(patten, iva):

            return str._new_(cls, iva)
        
        else: 

            raise ValueError('DIoni')
        
class Telefono(str):

    def _new_(cls, telefono: str):

        pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
        if re.match(pattern, telefono):

            return str._new_(cls, telefono)
        
        else:

            raise ValueError('Inserire un numero di telefono valido')
        
class Email(str):

    def _new_(cls, email: str):

        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        if re.match(pattern, email):

            return super()._new_(cls, email)
        
        else:

            raise ValueError('Inserire un email valida')

class Aliquota(float):

    def _new_(cls, aliquota: float):

        if 0 < aliquota <= 1:

            return super()._new_(cls, aliquota)
        
        else:

            raise ValueError('Inserire  un aliquota valida!')
        
