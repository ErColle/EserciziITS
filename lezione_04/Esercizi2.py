# # 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
# # Call the function, and make sure the message displays correctly.

# def display_message():
    
#     print("Today we learned python!")
    
# display_message()


# # 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title.
# # The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
# # Call the function, making sure to include a book title as an argument in the function call.

# def favorite_book(title):
#     print(f"My favourite book is {title}")
    
# favorite_book("Alice in Wonderland")

# # 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# # The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# # Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# def make_tshirt(size, message):
#     print(f"Tshirt\nSize: {size}, Message: {message}")

# make_tshirt("XS", "Dio merda")

# make_tshirt(size = "M", message = "Che fatica la vita da bomber!")


# # 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# # Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# def make_shirt(size, message = "I love Python!"):
#     print(f"Tshirt\nSize: {size}, Message: {message}")
    

# make_shirt("M")

# make_shirt("L")

# make_shirt("XS", "Assurdo!")


# # 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
# # The function should print a simple sentence, such as Reykjavik is in Iceland. 
# # Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

# def describe_city(name, country = "Italia"):
#     print(f"{name} is in {country}")

# describe_city("Roma")
# describe_city("Napoli")
# describe_city("Londra", "England")

# # 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
# # The function should return a string formatted like this: "Santiago, Chile".
# # Call your function with at least three city-country pairs, and print the values that are returned.
    
# def city_country(city, country):
#     return city, country

# print(*city_country("Milano", "Italia"))
# print(*city_country("Londra", "Inghilterra"))
# print(*city_country("Parigi", "Francia"))

# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the  dictionaries are storing the album information correctly. 
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.

# def make_album(artist, title, songs=None):
#     album = {'artist': artist, 'title': title}
#     if songs:
#         album['songs'] = songs
#     return album

# a1 = make_album("Lazza", "Sirio")
# a2 = make_album("Sfera", "Famoso", 11)
# a3 = make_album("Capo", "20")

# print(f"{a1}\n{a2}\n{a3}")


# 8-8. User Albums: Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

# def make_album(artist, title, songs=None):
#     album = {'artist': artist, 'title': title}
#     if songs:
#         album['songs'] = songs
#     return album

# risposta = None

# while risposta != "No" and risposta != "no":
    
#     artista = str(input("Inserisci Nome artista: "))
#     canzone = str(input("Inserisci nome canzone: "))
    
#     print(make_album(artista, canzone))
    
#     risposta = input("Vuoi inserire un altro album? Si/No: ")


# 8-9. Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

# messages = ["Ciao", "Ciao come stai", "Che bella giornata!"]

# def show_messages(messaggi):
#         print(messaggio)

# for messaggio in messages:
#     show_messages(messaggio)



# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

# messages = ["Ciao", "Ciao come stai", "Che bella giornata!"]

    
# def send_messages(messages):
    
#     i = 0

#     sent_messages = [] 
    
#     while messages:
#         messaggio = messages.pop(0) 
#         sent_messages.append(messaggio)
        
#         print(f"{messages=}\n{sent_messages=}\n\n")


# send_messages(messages)
        

# 8-11. Archived Messages: Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

# messages = ["Ciao", "Ciao come stai", "Che bella giornata!"]
# new_list = None
    
# def send_messages(messages):
    
#     i = 0

#     sent_messages = [] 
    
#     while messages:
#         messaggio = messages.pop(0) 
#         sent_messages.append(messaggio)
        
#         print(f"{messages=}\n{sent_messages=}\n\n")
    
    
#     return sent_messages


# newlist = send_messages(messages)
# print(f"La nuova lista è: {newlist}")


# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. Call the  function three times, using a different number of arguments each time.

# def order(*args):
#     items = [args]
    
#     print(f"Order summary:\n{items}")

# order1 = order("pizza", "pollo", "patatine")  
# order2 = order("cocacola", "fanta", "sprite")  
# order3 = order("pasta", "formaggio", "pane")  

# 8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you. 
# All the values must be passed to the function as parameters. 
# The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

# def build_profile(first_name, last_name, age, hair_color, weight):
#     return f"{first_name} {last_name}, age {age}, hair {hair_color}, weight {weight}\"  "

# carlofalco = build_profile("Carlo", "Falco", "59", "black", "60")
# print(carlofalco)

# 8-14. Cars: Write a function that stores information about a car in a dictionary. T
# he function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
# Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
# Print the dictionary that’s returned to make sure all the information was stored correctly. 


# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.


# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *