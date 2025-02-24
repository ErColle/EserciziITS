#Esercizio 1
#Scrivere un programma che permetta all'utente di inserire una serie di parole in input,
#terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
#Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.

parola = ""

while parola != "fine":
    parola = input("Inserisci una parola: ")
    if parola[0] == parola[-1]:
        print("Il primo e l'ultimo carattere sono uguali")
    else:
        print("Il primo e l'ultimo carattere non sono uguali")
    