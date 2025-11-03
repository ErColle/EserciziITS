# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merged = dict1.copy()
    
    for key, value in dict2.items(): 
        if key in merged:
            merged[key] = dict1[key] + dict2[key]
        else: 
            merged[key] = value

    return merged

	
print(merge_dictionaries({'a': 1, 'b': 3}, {'c': 4}))
