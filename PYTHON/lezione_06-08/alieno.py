class Alieno:
    '''
    
    Di un alieno ci interssa sapere la galassia di provenienza 
    self.galaxt: str 
    
    '''
    
# inizializzare un oggetto della classe Alieno 
    def __init__(self, galaxy: str):
        self.SetGalaxy(galaxy)
    
# definire un metodo per impostare il valore dell'attributo self.galaxy
    def SetGalaxy(self, galaxy):
        if galaxy:   #--> controllo se la stringa è vuota o no 
            self.galaxy = galaxy
        else:
            print("Errore! La galassia non può essere una stringa vuota!")
            
# definire metodo per restituire il valore dell'attributo self.galaxy
    def GetGalaxy(self):
        return self.galaxy  
    
# definire un metodo speak

    def speak(self):
        print("&/&%$%/$£%&/£$W/(&=&)(&&$$""%&(&")




 