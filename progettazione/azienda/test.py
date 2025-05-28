from beartype import beartype

from custom_types import *
from dipartimento import Dipartimento
from impiegato import Impiegato
from datetime import date, timedelta

@beartype
def test():
    tel1: str = "3334445566"
    tel2: str = "3456789012"

    ind: Indirizzo = Indirizzo("Viale Cesare Pavese", "305f",
                               CAP("00144"))

    dip1: Dipartimento = Dipartimento("Acquisti", tel1, ind)
    print(dip1)
    dip2: Dipartimento = Dipartimento("Vendite", tel2, ind)
    dip2.remove_indirizzo() # equivalente a dip2.set_indirizzo(None)
    dip2.add_telefono(tel1)
    print(dip2)
    alice: Impiegato = Impiegato(nome="Alice", cognome="Alessi",
                                 nascita=date.today()-timedelta(days=1),
                                 stipendio=RealGEZ(18000))

    bob: Impiegato = Impiegato(nome="Bob", cognome="Burnham",
                               nascita=date.today()-timedelta(days=2),
                               stipendio=RealGEZ(19000))
    print(alice)
    alice.set_nome("Alessia")
    print(alice)

    print(bob)
    # Non dà errore perché non abbiamo istruito beartype per controllare il typing in Impiegato
    alice.set_nome(False)
    print(alice)
