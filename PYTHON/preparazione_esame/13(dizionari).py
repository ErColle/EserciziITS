# Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario.
# Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:

    dict = {}
    for elem in tuples:
        if elem[0] not in dict:
            dict[elem[0]] = [elem[1]]
        else: 
            dict[elem[0]].append(elem[1])
            
    return dict

