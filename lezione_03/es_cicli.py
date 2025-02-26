# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

# pizze = ["Margherita", "Diavola", "Quattro Stagioni"]
# for pizze in pizze:
#     print(f"I like {pizze} pizza.")
# print("I really love pizza!")

# 4-2. Animals: Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. 
# You could print a sentence, such as Any of these animals would make a great pet!

# animals = ["cane", "gatto", "coniglio"]
# for animals in animals:
#     print(f"Il {animals} è il migliore aninali da compagnia.")

# print("Tutti questi animali sono animali da compagnia.")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

# for number in range(1, 21):
#     print(number)


# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

# numbers = list(range(1, 1000001))
               
# for numbers in numbers:
#     print(numbers)

# print(numbers)

# 4.5. Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.

# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number.

# for number in range(1, 21, 2):
#     print(number)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

# for number in range(3, 31, 3):
#     print(number)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

# list =[ 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000] 
# for num in list:
#     print(num)


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

# i = 1
# list =[] 
# for i in range (1, 11):
#     list.append(i**3)
#     i += 1

# print(list)

# # 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# # • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# # • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# # • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

# pizze = ["Margherita", "Diavola", "Quattro Stagioni", "Boscaiola", "Wustel e patatine", "Marinara", "Rossa", "Crostino", "Pepperoni"] 

# # for pizze in pizze:
# #     print(f"I like {pizze} pizza.")
# # print("I really love pizza!")

# print(pizze[:3])
# print(pizze[-3:])
# print(pizze[3:6])


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. 
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

# pizze = ["Margherita", "Diavola", "Quattro Stagioni"]
# for pizza in pizze:
#     print(f"I like {pizza} pizza.")
# print("I really love pizza!")

# pizze.append("Boscaiola")
# pizza_friend =["Marinara", "Carbonara", "Gamberetti"]
# print(f"My Favourite pizzas are:") 

# for pizza in pizze:
#     print(pizza)
# print(f"My friend's favourite pizzas are:")
# for pizza_friend in pizza_friend:
#     print(pizza_friend)

# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space.
# Choose a version of foods.py, and write two for loops to print each list of foods.


# 4-14. PEP 8: Look through the original PEP 8 style guide at https://peps.python.org/pep-0008/. 
# You won’t use much of it now, but it might be interesting to skim through it.

