class Documento: 
    
    def __init__(self, testo: str):
            self.setText(testo)
        
    def getText(self): 
        return self.testo
    
    def setText(self, testo: str):
        if testo is None:
            self.testo = ""
        else:
            self.testo = testo
        
    def isInText(self, keyword: str):
        if keyword.lower() in self.testo.lower():
            return True 
        else: 
            return False


class Email(Documento):
    
    def __init__(self , mittente: str, destinatario: str, titolo_messaggio: str, testo: str):
        
        super().__init__(testo)
        self.mittente = mittente 
        self.destinatario = destinatario
        self.titolo_messaggio = titolo_messaggio
    
    def getMittente(self):
        return self.mittente
    
    def getDestinatario(self):
        return self.destinatario
    
    def getTitoloMessaggio(self):
        return self.titolo_messaggio
    
    def setMittente(self, mittente: str):
        self.mittente = mittente
        
    def setDestinatario(self, destinatario: str):
        self.destinatario = destinatario
    
    def setTitoloMessaggio(self, titolo_messaggio: str):
        self.titolo_messaggio = titolo_messaggio
        
    def getText(self):
        return f"Da: {self.mittente}, A: {self.getDestinatario()}\nTitolo: {self.getTitoloMessaggio()}\nMessaggio: {self.testo} "
    
    def writeToFile(self):
        
        PATH: str = "PYTHON/esercizipotenziamento/testi_digitali.txt"
        mode: str = "w" 
        encoding: str = "utf-8"

        file = open(PATH, mode=mode, encoding=encoding)
        
        output: str = file.write(self.getText())   
        print(output)
        file.close
        

class File(Documento):
    
    def __init__(self, nomePercorso: str, testo):
        
        super().__init__(testo)
        self.nomePercorso = nomePercorso
        
        with open(self.nomePercorso, mode="w", encoding="utf-8") as file:  
            
                message: str = "Questo è il contenuto del file!"
                file.write(message)
                
                
    
    def leggiTestoDaFile(self):
        with open(self.percorsoCompleto, "r", encoding="utf-8") as f:
            self.testo = f.read()

    def getText(self):
        return f"Percorso: {self.nomePercorso}\nContenuto: {self.testo}"
    
documento = Documento("TESTO DELL'EMAIL!!. ")

email = Email("mittente@gmail.com", "destinatario@gmai.com", "Oggetto Mail", documento.getText())

print(email.getText())
                
file = File("PYTHON/esercizipotenziamento/document.txt", documento.getText())

print(file.getText())

print(email.isInText("TESTO"))
print(email.isInText("TESTOciao"))

print(file.isInText("TESTO"))
print(file.isInText("TESTOciao"))



        





    