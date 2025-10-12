def flatten_once(nested: list) -> list:
    new_lista = []
    for elem in nested:
        if isinstance(elem, list):
            new_lista.extend(elem)
        else:
            new_lista.append(elem)
    return new_lista

print(flatten_once([1, 2, 3, 4, [1, 2, 3, 5], [1, 2, 3]]))

