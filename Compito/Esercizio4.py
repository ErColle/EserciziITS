#Esercizio 4
#Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
#L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

#Il programma deve:

#Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
#Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).

num: float = 0
media: float = 0
somma: float = 0
count: int = 0
num = float(input("Inserisci un numero: "))
min = max = num
while num >= 0:
    
    if num.is_integer():
        somma += num
        count += 1
    if num < 0:
        somma -= num
        count -= 1
    
    if num < min:
        min = num
        
    if num > max:
        max = num
    num = float(input("Inserisci un numero: "))


    media = somma / count


print("La media dei numeri interi inseriti è:", media)
print("Il numero più grande tra quelli inseriti è:", max)
print("Il numero più piccolo tra quelli inseriti è:", min)
