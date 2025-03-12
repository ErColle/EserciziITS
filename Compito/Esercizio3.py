#Esercizio 3
#Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale.
#Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.

stringa = str(input("Inserisci una stringa: "))
stringa_invertita = ""

for i in range(len(stringa)-1 , -1  , -1  ):
    stringa_invertita += stringa[i]
    
print(stringa_invertita)
    