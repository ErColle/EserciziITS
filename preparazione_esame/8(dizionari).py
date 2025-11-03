# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.


def frequency_dict(elements: list) -> dict:
    dict = {}
    for elem in elements: 
        if elem not in dict:
            dict[elem] = 1
        else:
            dict[elem] += 1 
    return dict

print(frequency_dict(['mela', 'banana', 'mela']))
