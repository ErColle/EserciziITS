def bubble_sort(list: list[int]):
    
    for _ in range(len(list)):
        for i in range(len(list)):
            if i == len(list)-1:
                break
            
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
   
    return list

list = [34, 7, 23, 32, 5, 62, 32, 32]

print(bubble_sort(list))
    