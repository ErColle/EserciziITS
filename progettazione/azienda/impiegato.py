from custom_types import RealGEZ

from datetime import date

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, # noto alla nascita
    _stipendio: RealGEZ # # noto alla nascita

    def __init__(self, nome:str, cognome:str, nascita: date, stipendio: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    def __str__(self) -> str:
        return (f"{self.nome()} {self.cognome()}, "
                f"nascita: {self.nascita()}, "
                f"stipendio: {self.stipendio()}")
