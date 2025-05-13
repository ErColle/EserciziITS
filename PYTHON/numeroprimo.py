def numero_primo(num: int):
    
    count = 0
    
    for i in range (1, num+1):
        
        if num % i == 0:
            count += 1
    
    if num == 0: 
        return False
    elif count == 2: 
        return True 
    else: 
        return False
    
print(numero_primo(7))
        
    