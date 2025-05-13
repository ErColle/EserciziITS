def f(n: int): 
    while n!=1:
        if n%2 == 0: 
            n /= 2 
        else: 
            n = (n*3)+1
        
        print(int(n))
            
f(10)