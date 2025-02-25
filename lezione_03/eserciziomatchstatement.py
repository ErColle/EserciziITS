# Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante il numero di neonati e utilizzi lo statement match 
# per fornire una risposta appropriata:

# - Se il numero inserito è 1, stampare "Congratulazioni!"
# - Se il numero inserito è 2, stampare "Wow! Gemelli!
# - Se il numero inserito è 3, stampare "Wow! Tre!"
# - Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
# - Se il numero inserito è 5, stampare "Incredibile! Cinque!"
# - Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.

# Expected Output:

# Inserire il numero di neonati: 2
# Wow! Gemelli!

# - - - - - - - - - - - - - - - - - -

# Inserire il numero di neonati: 5
# Incredibile! Cinque!

# - - - - - - - - - - - - - - - - - -

# Inserire il numero di neonati: 7
# Non ci credo! 7 bambini!

# num = int(input("Inserisci il numero di bambini nati: "))

# match num:
#     case 1:
#         print("Congratulazioni!")
#     case 2:
#         print("Wow! Gemelli")
#     case 3:
#         print("Wow! Tre!")
#     case 4:
#         print("Mamma mia Quattro! Wow")
#     case 5:
#         print("Incredibile! Cinque!")
#     case _:
#         print(f"Non ci credo! {num} bamnbini!")

# Esercizio 3C-00B. Scrivere un programma in Python che chieda all'utente di inserire il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) 
# e utilizzi lo statement match per fornire una risposta adeguata da inserire in un documento di identita'.

# - Se il valore di gender è "m", stampare il nome e il genere come Maschio.
# - Se il valore di gender è "f", stampare il nome e il genere come Femmina.
# - Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando che non è possibile generare un documento di identità.

# Expected Output:

# Inserire nome: Luca
# Inserire gender. Digitare m per maschio e f per femmina: m
# Nome: Luca
# Gender: Maschio

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Inserire nome: Anna
# Inserire gender. Digitare m per maschio e f per femmina: f
# Nome: Anna
# Gender: Femmina

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Inserire nome: Alex
# Inserire gender. Digitare m per maschio e f per femmina: x
# Mi dispiace Alex, non e' possibile procedere con la generazione di un documento di identità!

# nome = str(input("Inserire nome: "))
# gender = str(input("Inserire gender. m per maschio f per femmina: "))

# match gender:
#     case "f":
#         print(f"Nome: {nome}\nGender: Femmina")
#     case "m": 
#         print(f"Nome: {nome}\nGender: Maschio")
#     case _:
#         print(f"Mi dispiace {nome}, non è possibile procedere con la generazione di un documento di identità! ")
    
# Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
# Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

# - 10 → "Eccellente"
# - 8-9 → "Molto buono"
# - 6-7 → "Sufficiente"
# - 4-5 → "Insufficiente"
# - 1-3 → "Gravemente insufficiente"
# - Altro caso → "Voto non valido"

# Expected Output:

# Inserisci il voto: 5
# Output: Insufficiente
# - - - - - - - - - - -
# Inserisci il voto: 11
# Output: Voto non valido

# voto = int(input("Inserisci il voto: "))

# match voto:
#     case 10:
#         print("Eccellente")
#     case 8 | 9:
#         print("Molto buono")
#     case 6 | 7:
#         print("Sufficiente")
#     case 4 | 5:
#         print("Insufficiente")
#     case 1 | 2 | 3:
#         print("Gravemente insufficiente")
#     case _:
#         print("Voto non valido")

# Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
# Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare 
# il corrispondente GPA americano, secondo questa tabella di conversione:

# - 106-110 → 4.0
# - 101-105 → 3.7
# - 96-100 → 3.3
# - 91-95 → 3.0
# - 86-90 → 2.7
# - 81-85 → 2.3
# - 76-80 → 2.0
# - 70-75 → 1.7
# - 66-69 → 1.0
# - Altro caso → "Voto non valido"

# Expected Output:

# Inserisci il voto di laurea: 110
# Output: GPA 4.0

# - - - - - - - - - - - - - - - - -

# Inserisci il voto di laurea: 65
# Output: Voto non valido

# voto = float(input("Inserisci voto: "))
# match voto:
#     case voto if 106 <= voto <= 110:
#         print("Voto GPA: 4.0") 
#     case voto if 101 <= voto <= 105:
#         print("Voto GPA: 3.7")
#     case voto if 96 <= voto <= 100:
#         print("Voto GPA: 3.3")
#     case voto if 91 <= voto <= 95:
#         print("Voto GPA: 3.0")
#     case voto if 86 <= voto <= 90:
#         print("Voto GPA: 2.7")
#     case voto if 81 <= voto <= 85:
#         print("Voto GPA: 2.3")
#     case voto if 76 <= voto <= 80:
#         print("Voto GPA: 2.0")
#     case voto if 70 <= voto <= 75:
#         print("Voto GPA: 1.7")
#     case voto if 66 <= voto <= 69:
#         print("Voto GPA: 1.0")
#     case _:
#         print("Voto non valido")
    

