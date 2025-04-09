
# LISTA

lista1: list = [1, 2, 3, 4, 5]
matrice: list = [[2, 1, 4], [5,3]]
print(matrice)


matrice[1].append("Ciao")
print(matrice)


# SET 

set1: set = { 1, 1, 2, 3, "Ciao", 4, 5,} # <---Non puo avere duplicati
print(set1) # <---DUPLICATI STAMPATI UNA SOLA VOTA + RIORDINA (ciao va alla fine)

#INTERSEZIONE UNIONE E DIFFERENZA SET

set_a = { 1, 2, 3, 4}
set_b = { 1, 2, 5, 6}

print(set_a.intersection(set_b)) #INTERSEZIONE (COMUNI UNA SOLA VOLTA)

print(set_a.union(set_b)) #UNIONE (COMUNI E NON COMUNI UNA SOLA VOLTA)

print(set_a.difference(set_b)) #DIFFERENZA (NON COMUNI UNA SOLA VOLTA)

#TUPLA

tupla: tuple = (1, 2, 3, 4, 5) # <---NON PUO ESSERE MODIFICATA
print(tupla)


#DICTIONARY 

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 20
}

print(persona) # <--I DUPLICATI VENGONO STAMPATI USA SOLA VOLTA


