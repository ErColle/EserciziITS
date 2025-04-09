#Exercise 1
#Write a function check_value(), which takes a number as an argument.
#Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.

def check_value(a: int):
    if a > 5:
        print(f"{a} is bigger than 5!")
    elif a < 5:
        print(f"{a} is lower than 5!")
    else:
        print(f"{a} is equal to 5!")
 
check_value(8)   

#Exercise 2
#Write a function check_length(), which takes a string as an argument.
#Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.

def check_lenght(word: str):
    if len(word) > 10: 
        print(f"The word {word} has more than 10 char")
    elif len(word) < 10: 
        print(f"The word {word} has less than 10 char")
    else: 
        print(f"The word {word} has 10 char")

check_lenght("1234567890")

#Exercise 3 
#Write a function print_numbers(), which takes a list of numbers as argument.
#Using a for loop, print each number one by one.

def print_numbers(*args):
    for numbers in args:
        print(numbers)

print_numbers(1, 2, 3, 4, 5, 6)

#Exercise 4
#Write a function check_each(), which takes a list of numbers as argument.
#Using a for loop, iterate through the list.
#For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5

def check_each(*args):
    for number in args:
        
        if number > 5:
            print(f"{number} is bigger than 5!")
        
        elif number < 5:
            print(f"{number} is lower than 5!")
            
        else:
            print(f"{number} is equal to 5!")

check_each(10, 5, 2)

#Exercise 5
#Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
#Write another function add_one_to_list(). It takes a list of integers as argument.
#Define a variable new_list in this function.
#Using a for loop, iterate through the argument list.
#Using add_one(), fill new_list with integers from the argument list incremented
#by 1.
#Print new_list.

def add_one(num: int) :
    num += 1
    return num

def add_one_to_list(*args):
    
    new_list = []
    
    for element in args: 
        new_list.append(add_one(element))
    
    print(new_list)
        
add_one_to_list(1, 2, 3, 4, 5, 6)
    






    