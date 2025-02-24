#Esercizio 10
#Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

#Il programma deve:

#acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
#calcolare e visualizzare la somma di tutti i numeri pari inseriti;
#calcolare e visualizzare la media di tutti i numeri dispari inseriti;
#determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
#se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

num: int = 1
somma = 0
media = 0
smedia = 0
nmedia = 0

while num != 0:
    num = int(input("Inserisci un numero (0 per terminare): "))
    if num % 2 == 0:
        somma += num
    
    if num % 2 == 1:
        smedia += num
        nmedia += 1
media = smedia / nmedia
print("La somma dei numeri pari e' ", somma)
print("La media dei numeri dispari e' ", media)

