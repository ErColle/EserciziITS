# Esercizio 1. 

# Scrivere in Python una funzione recursivePower che calcola la potenza di un numero utilizzando la ricorsione. 
# La funzione deve ricevere due parametri in input:

# base: il numero da elevare a potenza.
# exponent: l’esponente a cui elevare la base.
# Utilizzare, poi, la funzione per calcolare:

# 3⁴, ovvero 3 elevato alla potenza di 4. 
# 43 , ovvero 4 elevato alla potenza di 3.
# 25, ovvero 2 elevato alla potenza di 5. 
# 52, ovvero 5 elevato alla potenza di 2.
 
# Esercizio 2.
# Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto.
# Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
# Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.
 
 
# Esercizio 3.

# Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

# n * (n-1) * (n-2) * ... * 1

# con 1! uguale a 1 e 0! definito come 1.
# Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.
 
 
# Esercizio 4.

# Scrivere una funzione ricorsiva recursiveDigitCounter che restituisca il numero di cifre di un numero intero n passato in input.
# Sono permessi sia valori positivi che negativi per n.
# Ad esempio, il numero -120 ha 3 cifre.
# Non si tenga conto di eventuali zeri non significativi.

# Suggerimento: per il calcolo delle cifre, fare un controllo se il valore assoluto di n sia minore di 10. In caso positivo, significa che il numero n ha una sola cifra. In caso negativo, significa che il numero n ha più cifre; dunque, dividere n per 10 per rimuovere l'ultima cifra e richiama ricorsivamente la funzione, fino a ottenere un numero con una sola cifra.
 
 
# Esercizio 5.

# Una progressione armonica è definita come il prodotto dei reciproci dei primi n numeri interi positivi, ovvero il risultato della moltiplicazione di 1 diviso ogni numero intero da 1 fino a n.
# Ad esempio, se n = 6, la progressione armonica A vale:
# A = 1/6 * 1/5 * 1/4 * 1/3 * 1/2 * 1 = 0.001389.

# Scrivere in Python una funzione ricorsiva chiamata armonica che dato un numero n intero positivo, calcoli la relativa progressione armonica, arrotondando il risultato finale a 6 cifre decimali.
 
 
# Esercizio 6.

# Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi una produttoria definita come segue:
# Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

# Calcolare il valore della produttoria Pi se n = 7.
 
 
# Esercizio 7.

# Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi3 una produttoria definita come segue:
# Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  

# Calcolare il valore della produttoria Pi3 se n = 5.
 
 
# Esercizio 8.

# Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

# Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
# L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.


def vowelsCounter(parola: str):
    
    vocali = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    i = 0
    
    if len(parola) == 0:
        
        return count
    else:
        if parola[i] in vocali: 
            i += 1
            count += 1
            return(parola[1:])
        
        vowelsCounter(parola)

print(vowelsCounter("ciao"))

 
 
# Esercizio 9.

# Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

# Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.
 
 
# Esercizio 10.

# Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa e restituisca il risultato sotto forma di una nuova stringa.

# Ad esempio, se la stringa "libro" viene data in input a charDuplicator, la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".