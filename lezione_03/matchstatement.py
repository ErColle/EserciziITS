#MATCH STATEMENT

posizione = int(input("Inserisci la posizione: "))

# if posizione == 1:
#     print(f"{posizione}st")
# elif posizione == 2:
#     print(f"{posizione}nd")
# elif posizione == 3:
#     print(f"{posizione}rd")
# else:
#     print(f"{posizione}th")
    
match posizione:
    case 1:
        print(f"{posizione}st")
    case 2:
        print(f"{posizione}nd")
    case 3:
        print(f"{posizione}rd")
    case _:
        print(f"{posizione}th")
        
# "OR" == |
# "AND" == &


a = 1
b = 2

match (a, b):
    
    case (1, 2):
        print("a is 1 and b is 2")
    case (1, 1):
        print("a is 1 and b is 1")
    
# STATEMENT LISTE E DIZIONARI

#LISTE
lista = [1, 2, 3, 4, 5]

match lista:
    case [1, 2, 3]:
        print("La lista contiene 1, 2 e 3")
    case [1, 2, 3, 4, 5]:
        print("La lista contiene 1, 2, 3, 4 e 5")
    case _:
        print("La lista non contiene 1, 2 e 3")
        
#DIZIONARI

dizionario = {"nome": "Mario", "cognome": "Rossi", "età": 30}

match dizionario:
    case {"nome": "Mario", "cognome": "Rossi"}:
        print("Il dizionario contiene Mario Rossi")
    case {"nome": "Mario", "cognome": "Rossi", "età": 30}:
        print("Il dizionario contiene Mario Rossi e ha 30 anni")
    case _:
        print("Il dizionario non contiene Mario Rossi")