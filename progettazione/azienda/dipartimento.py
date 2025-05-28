from custom_types import Indirizzo
from citta import Citta

class Dipartimento:

    _nome: str # noto alla nascita
    _telefoni: set[str] # [1..*] (e quindi noto alla nascita)
    _indirizzo: Indirizzo # mutabile, [0..1], certamente noto alla nascita
    _citta: Citta # noto alla nascita

    def __init__(self, nome: str, telefono: str, indirizzo: Indirizzo,
                 c: Citta) -> None:
        self.set_nome(nome)

        self._telefoni = set()
        self.add_telefono(telefono)

        self.set_indirizzo(indirizzo)
        self.set_citta(c)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def telefoni(self) -> frozenset[str]:
        return frozenset(self._telefoni)
    
    def add_telefono(self, telefono: str) -> None:
        self._telefoni.add(telefono)

    def remove_telefono(self, t: str) -> None:
        if len(self.telefoni()) == 1:
            raise RuntimeError('Il dipartimento deve avere almeno un numero di telefono')
        elif t not in self.telefoni():
            raise KeyError(f"Non posso rimuovere il numero di telefono {t} che non appartiene al dipartimento")

        self._telefoni.remove(t)

    def indirizzo(self) -> Indirizzo:
        return self._indirizzo
    
    def set_indirizzo(self, indirizzo: Indirizzo|None) -> None:
        self._indirizzo = indirizzo

    def remove_indirizzo(self) -> None:
        self.set_indirizzo(None)

    def citta(self) -> Citta:
        return self._citta

    def set_citta(self, c: Citta) -> None:
        self._citta = c



    def __repr__(self) -> str:
        return f'Dipartimento({self._nome}, {self._telefoni}, {self._indirizzo}, {self._citta})'

    def __str__(self) -> str:
        if self.indirizzo():
            ind_str: str = "con sede in " + str(self.indirizzo())
        else:
            ind_str: str = "senza sede"

        tel_str: str = "[" + ", ".join(self.telefoni()) + "]"

        return f"Dipartimento '{self.nome()}' {ind_str} a {self.citta()} e numeri di telefono: {tel_str}"
