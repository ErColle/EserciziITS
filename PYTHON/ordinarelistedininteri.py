def order_list(list: list[int]):
    
    temp = None
    
    for i in range(0, len(list)+1):
        
        if list[i] > list[i+1]:
            temp = list[i] 
            list[i] = list[i+1]
            list[i+1] = temp  
        
    return list

list = [ 4, 2, 5, 6, 7, 8, 9]

order_list(list) 
    