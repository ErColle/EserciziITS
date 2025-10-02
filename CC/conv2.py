stringa: str = "ciao"
# ciao = int(stringa, 2)  # Removed invalid conversion
# print(ciao)


def S2N(s: str): 
    base = 1 
    n = 0 
    for char in s:
        n = n + base * ord(char)
        base = base * 2

    return n 

print(S2N(stringa))

def N2S(num):
    
    stringa = ""
    
    while num > 0:
        char = num % 2
        stringa += chr(char)
        num = num // 2 # Use integer division
        
    return stringa  # Reverse the string to get the original

print(N2S(S2N(stringa)))
        
    