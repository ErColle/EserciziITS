# 9-1. Restaurant: Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# class Restaurant:
    
#     def __init__(self, restaurant_name, cuisine_type ):
        
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
        
#     def describe_restaurant(self):

#         print(self.restaurant_name, self.cuisine_type)
        
#     def open_restaurant(self):
#         print("Restaurant is open!")
    

# restaurant = Restaurant("McDonald's", "Fast food")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()



# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type ):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):

        print(self.restaurant_name, self.cuisine_type)
        
    def open_restaurant(self):
        print("Restaurant is open!")
    

mcdonald = Restaurant("McDonald's", "Fast food")
piadineria = Restaurant("Piadineria", "Italian piadine")
pokehouse = Restaurant("Poke House", "Poke food")

mcdonald.describe_restaurant()
piadineria.describe_restaurant()
pokehouse.describe_restaurant()



# 9-3. Users: Make a class called User. 
# Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user.

# 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
