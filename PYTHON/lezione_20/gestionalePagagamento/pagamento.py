from datetime import data

class Pagamento: 
    def __init__(self, importo:float):
        self.__importo = importo
        
    def setImporto(self, importo:float):
        self.__importo = importo
        
    def getImporto(self):
        return self.__importo

    def dettagliPagamento(self):
        return f"Importo del pagamento: {self.__importo} euro"
    
class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__(importo)
        
    def dettagliPagamento(self):
        return f"Importo del pagamento: {self.getImporto()} euro in contanti"  
      
    def inPezziDa(self):
        banconote = [500, 200, 100, 50, 20, 10, 5]
        monete = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        importo = self.getImporto()        
        listabanconote = {}  
        
        for i in banconote:
            if importo >= i:
                listabanconote[i] = int(importo // i)
                importo = round(importo % i, 2)
                
        for i in monete:
            if importo >= i:
                listabanconote[i] = int(importo // i)
                importo = round(importo % i, 2)
                
        for taglio in sorted(listabanconote.keys(), reverse=True):
            quantita = listabanconote[taglio]
            tipo = "banconota" if taglio >= 5 else "moneta"
            print(f"{quantita} {tipo} da {taglio} euro")

        return None

class PagamentoCartaDiCredito(Pagamento):
    
    def __init__(self, importo, nomeTitolare: str, dataScadenza:data, numeroCarta: str ):
        super().__init__(importo)
        self.nomeTitolare = nomeTitolare
        self.dataScadenza = dataScadenza
        self.numeroCarta = numeroCarta
        
    def dettagliPagamento(self):
        return f"Pagamento di: {self.__importo} effettuato con la carta di credito\nNome sulla carta: {self.nomeTitolare} \nData di scadenza: {self.dataScadenza}\nNumero della carta: {self.numeroCarta}"
        
        
        
        
pagamento = Pagamento(0)
pagamento.setImporto(100)
print(pagamento.dettagliPagamento())

pagamentocontanti = PagamentoContanti(0)
pagamentocontanti.setImporto(1600.01)
print(pagamentocontanti.dettagliPagamento())

pagamentocontanti.inPezziDa()

pagamento_carta = PagamentoCartaDiCredito(250.75,"Mario Rossi","1234 5678 9012 3456",2026, 12, 31)

print(pagamento_carta.dettagliPagamento())


             
                

