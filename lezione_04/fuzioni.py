# #Sum of integers from 1 to  10 

# sum: int = 0 
# for i in range(1, 11):
#     sum += i
# print(f"Sum of integers from 1 to 10: {sum}")
# #Sum of integers from 20 37 

# sum: int = 0
# for i in range(20, 38):
#     sum += i
# print(f"Sum of integers from 20 to 37: {sum}")

# #Sum of integers from 35 to 49

# sum: int = 0 
# for i in range (35, 50):
#     sum += i
# print(f"Sum of integers from 35 to 49: {sum}")

#Come definire una funzione in Python

def nome_funzione ( a:int, b:int ): #Parametri tra parentesi
     
    result: int = 0
    for i in range (a, b+1):
        result += i                   #Istruzioni da eseguire 
    return result


print(nome_funzione(1, 10))
print(nome_funzione(20, 38))
print(nome_funzione(35, 49))

# Let’s try to define a function named subtract ourselves:
# ● It should take 2 parameters.
# ● Inside the function, it should subtract the two.
# ● Then, return the result.

def subtract( a, b):
    return a - b

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print(f"Substract: {subtract(num1, num2)}")










