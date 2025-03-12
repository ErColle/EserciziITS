#Esercizio 6
#Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

#Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.

n1 = int(input("Inserisci primo numero: "))
n2 = int(input("Inserisci secondo numero: "))
prod = 1

if n2 > n1: 
    for num in range( n2, n1+1):
        result = prod*num
        print(f"{prod} * {num} = {result}")
        prod = result
