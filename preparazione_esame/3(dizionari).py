# Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dict = {"pari": [], "dispari": []}   
    for num in lista:
        if num % 2 == 0:
            dict["pari"].append(num)
        else:
            dict["dispari"].append(num)
            
    return dict

	
print(classifica_numeri([1, 2, 3, 4, 5, 6]))