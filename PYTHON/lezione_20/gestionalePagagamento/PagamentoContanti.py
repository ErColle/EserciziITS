from pagamento import Pagamento 

class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__(importo)
        
    def dettagliPagamento(self):
        return f"Importo del pagamento: {self.__importo} euro in contanti"
    
    def inPezziDa(self):
        self
