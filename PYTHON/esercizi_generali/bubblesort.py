def bubble_sort(lista):
    
    for _ in range(len(list)):
        for i in range(len(list)):
            if i == len(list)-1:
                break
            
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
   
    return list

lista = [34, 7, 23, 32, 5, 62, 32, 32]

print(bubble_sort(lista))
    