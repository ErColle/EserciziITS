lista1: list = [1, 2, 3, 4, 5]
matrice: list = [[2, 1, 4], [5,3]]
print(matrice)

#INSERISCE ALLA LISTA  VALORE 6 ALLA FINE 

lista1.append(6)
print(lista1)

matrice[1].append("Ciao")
print(matrice)

#FUNZIONE LEN NUMER CARATTERI STRINGA

print(len(lista1))
print(len(matrice[0]))

#SOMMA DI DUE LISTE 

a: list = [1, 2]
b:list = [3, 4]

a += b #equivalente a.extend(b)
print(a)

# SET 

set1: set = { 1, 1, 2, 3, "Ciao", 4, 5,} # <---Non puo avere duplicati
print(set1) # <---DUPLICATI STAMPATI UNA SOLA VOTA + RIORDINA (ciao va alla fine)

#INTERSEZIONE UNIONE E DIFFERENZA SET

set_a = { 1, 2, 3, 4}
set_b = { 1, 2, 5, 6}

print(set_a.intersection(set_b)) #INTERSEZIONE (COMUNI UNA SOLA VOLTA)

print(set_a.union(set_b)) #UNIONE (COMUNI E NON COMUNI UNA SOLA VOLTA)

print(set_a.difference(set_b)) #DIFFERENZA (NON COMUNI UNA SOLA VOLTA)

#DICTIONARY 

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 20
}

print(persona) # <--I DUPLICATI VENGONO STAMPATI USA SOLA VOLTA

#RIMUOVI ELEMENTO 

persona.pop("eta")
print(persona)

#AGGIUNGI ELEMENTO 

persona["eta"] = 19
print(persona)

#MODIFICA ELEMENTO 

persona["eta"] = 20 
print(persona)