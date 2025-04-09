#CONDIZIONI

a = 5
b = 4

if ( a < b): 
    print("suca")
elif (a > b):
    print("merda")
else:   
    print("ciao")


#CICLI


lista1: list = ["a", "b", "c"]
lista2: list = [1, 2, 3]

for lettera in lista1:
    for numero in lista2:
        print(lettera, numero)

for lettera in lista1:  # <-- numero è una nuova variabile che prende il valore di ogni elemento della lista
    print(lettera) 



for lettera in lista1:
    for numero in lista2:
        print(lettera, numero)

l = [[("a", 1), ("a", 2), ("a", 3)], [("b", 1), ("b", 2), ("b", 3)], [("c", 1), ("c", 2), ("c", 3)]] # <-- lista di liste (matrice)


#ACCESSO TRAMITE INDICI

print(l[0][0]) # <-- a1 

for i in range(3):  # <-- range genera una lista di numeri da 0 a 2 (3) ( [0, 1, 2] )dhhdsss
    for j in range(3):
        print(l[i][j])
#esempio primo ciclo --> i = 0, j = 0 --> l[0][0] --> l["a1"] = a1
#esempio secondo ciclo --> i = 0, j = 1 --> l[0][1] --> l["a2"] = a2


#STAMPA NUMERI PARI LISTA 2

for num in lista2:
    if num % 2 == 0:
        print(num)
#esempio primo ciclo --> num = 1 --> 1 % 2 == 0 --> False non stampa
#esempio secondo ciclo --> num = 2 --> 2 % 2 == 0 --> True stampa 2

#RANGE
lista3: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in range(0, 8, 2): # da 0 a 8 con step di 2 
    print(lista3[number])

#ESEMPIO DI STAMPA LISTA DEI NUMERI PARI CON RANGE 
for number in range(1, 10, 2):
    print(lista3[number])

# CICLO WHILE

x = 0
while x < 5:  # ESEGUE IL CICLO FINCHE' x < 5
    print("Valore di x:", x)
    x += 1  # INCREMENTA X DI 1



