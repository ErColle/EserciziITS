from custom_types import RealGEZ

class Progetto:

    _nome: str # noto alla nascita
    _budget: RealGEZ # noto alla nascita

    def __init__(self, nome: str, budget: RealGEZ) -> None:
        self._nome = nome
        self._budget = budget

    def nome(self) -> str:
        return self._nome

    def budget(self) -> RealGEZ:
        return self._budget

    def get_nome(self) -> str:
        return self._nome

    def get_budget(self) -> RealGEZ:
        return self._budget

    def __str__(self) -> str:
        return f"Progetto '{self.nome()}' con budget: {self.budget()}€"

    def __repr__(self) -> str:
        return f"Progetto(nome={self.get_nome()}, budget={self.budget()})"