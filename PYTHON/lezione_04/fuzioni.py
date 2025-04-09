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

# def subtract( a, b):
#     return a - b

# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))
# print(f"Substract: {subtract(num1, num2)}") 

#FUNZIONE SENZA RETURN 

def display_info(info: str) -> None: 
    print("info")

print("ciao")



def multireturn ( a: int, b: int):
    return [a, b],[b, a]

print(multireturn(10,20))  

#Default input nei parametri 

def funzione(par1: int, par2: int, par3: int = 1, par4:int = 2):
    print ( par1, par2 , par3, par4)

print("Parametri con  par3 e par4 di default nella funzione senza definirli: ")
funzione(par1 = 1, par2 = 2) #NO(N METTO PAR3 E PAR4 DATO CHE HANNO GIA VALORE 1 E 2
print("Parametri con  par3 e par4 di default nella funzione definiti nel richiamo della funzione: ")
funzione(par1 = 1, par2 = 2, par3 = 3, par4 = 4) 

#Fuzioni senza parametri 

def hello():
    print("Hello")
    
hello()

#Massimo tra 2 numeri 

def max(num1: int, num2: int):
    if num1 > num2:
        return num1
    else: 
        return num2

num_max = max(30, 20)
print(num_max)

#Funzione args

def add(*args):  #Numero indefinito di parametri
    print(args)

add( 1, 2, 3, 4, 5, 6, 7)

#Somma dei numeri in args 

def add_sum(*args):
    somma = 0 
    for numbers in args:
        somma += numbers
    return somma

somma = add_sum(1, 2, 3, 5)
print(somma)

#Funzione kwargs per collections 

def total(**kwargs):
    print(kwargs)
    
total(caffe = 10, cappuccino = 20)

#FUNZIONE RICORSIVA 

def conto_alla_rovescia(n):
    if n <= 0:  # Caso base: quando n è 0, smettiamo di chiamare la funzione
        print("BOOM!")
    else:
        print(n)
        conto_alla_rovescia(n - 1)  # Passo ricorsivo --> RICHIAMA LA FUNZIONE STESSA PER RIPETERLA

conto_alla_rovescia(5)

    


        
  











