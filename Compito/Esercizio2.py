#Esercizio 2
#Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa.
#Il risultato deve essere visualizzato in output.

stringa = str(input("Inserisci una stringa: "))
count = 0
for i in stringa:
    if i == " ":
        count += 1
print ("Il numero totale di spazi presenti nella stringa è:", count)