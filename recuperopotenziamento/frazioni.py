# 8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.

# Si definiscano i metodi __init__, setter, getter, __str__, value.
# In particolare:
# il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;
# il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
# i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. 
# Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.
# Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer() e isistance().


# 8.C Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, 

# ovvero il più grande divisore comune tra numeratore e denominatore è 1.

# Sia l una lista di frazioni, ovvero una lista di oggetti della classe Frazione.

# Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di frazioni ritorni in output una lista di frazioni irriducibili.
 
# Nello specifico:
# -se una frazione f della lista data in input è già irriducibile, allora inserire questa frazione f nella lista da ritornare in output.
 
# -se una frazione f della lista data in input può essere semplificata, in una frazione irriducibile f1, allora si deve prima semplicare la frazione f, 
# ottenendo la frazione irriducibile f1 e poi inserire f1 nella lista da ritornare in output.

# Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione semplifica.
# Inserire in modo adeguato le seguenti frazioni nella lista l.

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.setNumeratore(numeratore)
        self.setDenominatore(denominatore)
        
    def setNumeratore(self, numeratore):
        if isinstance(numeratore, int):
            self.numeratore = numeratore
        else: 
            self.numeratore = 13

    def getNumeratore(self):
        return self.numeratore
    
    def setDenominatore(self, denominatore):
        if isinstance(denominatore, int) and self.denominatore != 0:
            self.denominatore = denominatore
        else: 
            self.denominatore = 5
    
    def getDenominatore(self):
        return self.denominatore
    
    def value(self):   
        frazione = self.numeratore / self.denominatore
        return round(frazione, 3)
    
    def __str__(self):
        return f"{self.numeratore} / {self.denominatore}"
    
def semplifica():
    pass