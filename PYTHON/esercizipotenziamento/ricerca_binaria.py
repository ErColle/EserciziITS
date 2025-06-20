def ricerca_binaria(numeri: list[int] , num: int):
    
    primo_elem = 0
    ultimo_elem = len(numeri) - 1
    

    i_centro = (ultimo_elem + primo_elem) // 2
    valore = numeri[i_centro] 
    
    while :
        
        if valore == num:
            return True
        
        elif num < valore:
            i_centro -= 1 
            valore = numeri[i_centro] 
        else: 
            i_centro += 1 
            valore = numeri[i_centro] 
            
    
    return False
        
print(ricerca_binaria([2, 4, 5, 6, 8, 9, 11, 13, 17], 3))

""" soluzione 

def binary_search(numeri: list, num: int):
    
    i, j = 0, -1
    
    mid = len(numeri) // 2 
    
    if numeri[mid] ==  num:
        return True
    
    if numeri[mid] > num:
        
        j = mid - 1
        binary_search( numeri[i:j], num )
        
    else:
        
        j = mid + 1
        binary_search( numeri[i:j], num ) """
        
        
                  