class Citta:
    _nome: str

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome