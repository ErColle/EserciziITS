# from matplotlib.pyplot import plt

def f(n: float):
    
    numeri: list = [n] 
    
    while n != 1:
        
        if n % 2 == 0:
            n /= 2
            
        else:
            n = (n * 3) + 1
            
        numeri.append(n)

    return numeri

print(f(5.0))
    
# numeri: list[float] = f(5.0) 

# plt.plot(numeri)
# plt.show()