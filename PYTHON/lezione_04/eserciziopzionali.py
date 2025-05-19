# 1. School Grading System:

#  Create a function that takes a student's name and their scores in different subjects as input.
# The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
# Create a for loop to iterate over a list of students and scores, calling the function for each student.

""" def scool_grading_system(name:str , scores:list):
    count = 0
    total = 0
    
    for score in scores: 
        count += 1
        total += score
        avg = total/count
        if avg >= 60:
            message = ("pass the exam!")
        else: 
            message = ("dont pass the exam!")
            
    return f"{name} has {avg} grade and he {message}"

student = "alessio"
scores = [30, 20, 50, 70] 

print(scool_grading_system(student, scores)) """
        
        
    
# 2. Guess the Number Game:

# Create a function that generates a random number within a range specified by the user.
# Prompt the user to guess the number within a specified maximum number of attempts.
# Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
# Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.4

            

# 3. E-commerce Shopping Cart:

# Create a function that defines a product with a name, price, and quantity.
# Create functions that manage the shopping cart, allowing the user to add, remove, and view products in the cart.
# Create a function that calculates the cart total and apply any discounts or taxes.
# Create a funciton to print a detailed summary of the cart including products and totals.
# Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

shopping_cart: dict = 


def denfines_product(name: str, price: int, quantity: int):
    print(f"Product name: {name}\nPrice: {price}\nQuantity: {quantity}")
    
def shopping_cart(product: dict):




# 4. Text Analysis:

# Create a function that takes a paragraph and counts the number of occurrences of each word.
# The function should print a report showing the most frequent words and their number of occurrences.
# You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.

# 5. Inventory Management System:

# Create a list to store the items in inventory.
# Create a function that defines an item with a code, name, quantity, and price.
# Implement functions to add, remove, search, and update items in the inventory.
# Use for loops to manage the various inventory operations.

# 6. Password Generator:

# Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
# Allow the user to specify the password length and desired character types.
# Generate and return a random password that meets the user's criteria.

# 7. Roman Numeral Conversion:

# Create a function that converts a given integer to its Roman numeral representation.
# Handle numbers from 1 to 3999.
# Use a combination of string manipulation and conditional statements to build the Roman numeral.
# 8. ATM Machine Simulator:

# Create a function that simulates an ATM machine.
# Initialize an account with a starting balance.
# Allow the user to perform transactions such as deposit, withdraw, and check balance.
#  Validate transactions against the account balance and available funds.
# Provide appropriate feedback to the user for each transaction.
# 9. Caesar Cipher Encryption/Decryption

# Create functions for encrypting and decrypting a message using the Caesar cipher.
# Allow the user to specify the shift value (number of positions to shift each letter).
#  Handle both encryption and decryption using the same function with appropriate adjustments.
# Encrypt and decrypt the given message using the specified shift value.
# 10. Anagram Checker:

# Create a function that checks whether two given strings are anagrams of each other.
# Convert both strings to lowercase and remove any non-alphabetic characters.
# Sort the characters of each string and compare the sorted strings for equality.
# Indicate whether the strings are anagrams or not.
# 11. Sieve of Eratosthenes Prime Number Generator:

# Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
# Initialize an array of all numbers up to the limit, marking each number as prime initially.
# Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
# The remaining unmarked numbers are the prime numbers within the limit.