#Esercizio 6
#Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

#Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
prodotto = 1
if n1 > n2:
    for i in range(n2, n1 + 1):
        prodotto *= i
else:
    for i in range(n1, n2 + 1):
        prodotto *= i
print("Il prodotto dei numeri compresi e' ", prodotto)
