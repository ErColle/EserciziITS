# 1. Copy the code and print the age of
# bob (using the dot notation)
# 2. Create an if-statement that prints
# the name of the oldest of the two
# Persons
# 3. Create three other Persons. Make
# a list called people with all 5
# Persons.
# 4. Make a loop that finds andson: prints
# the youngest person’s name
print("Esercizio 1\n")

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
             
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
mark = Person("Mark S.", 21)
jane = Person("Jane D.", 30)
joe = Person("Joe B.", 20)

people = [alice, bob, mark, jane, joe]

youngest = people[0]

for person in people:
    if youngest.age > person.age:
        youngest = person

print(youngest.name)

print(bob.age)

if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)
    
# Exercise 2 (Folder 9 ex_2.py)
# 1. Write a class called Student with the attributes name (str) and
# studyProgram (str)
# 2. Create three instances. One for yourself, one for your left neighbour and one
# for our right neighbour.
# 3. Add a method printInfo that prints the name and studyProgram of a
# Student. Test your method on the objects!
# 4. Modify the code and add age and gender to the attributes. Modify your
# printing methods respectively too

print("\n\n\n\nEsercizio 2\n\n")

class Student: 
    
    def __init__(self, name, studyProgram, age, gender):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender 
    
    def printInfo(self):
        
        print(f"Study Program: {self.studyProgram}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}")
        
me = Student("Ale", "FullStack", 20, "M")
neighbour1 = Student("Bob", "CyberSecurity", 21, "M")
neighbour2 = Student("Alice", "VideoEdit", 22, "F")

Student.printInfo(me)


    # Exercise 3 (Folder 9 ex_3.py)
    # Given is the class Animal. For each task, test your changes!
    # 1. Create two realistic instances of Animals
    # 2. Print the name of each object
    # 3. Change the amount of legs of one object using the dot notation
    # 4. Add a method setLegs() to set the legs of an object and repeat task 3 but
    # this time using the method.
    # 5. Add a method getLegs() to return the amount of legs
    # 6. Add a method named printInfo that prints all attributes of the Animal

print("\n\n\n\nEsercizio 3\n\n")

class Animal:
    
    def __init__(self, name, legs):
        self.name = name
        
    def setLegs(self, legs):
        self.legs = legs 
        
    def getLegs(self):
        return self.legs
    
    def printInfo(self):
        print(self.name, self.legs)


tigre = Animal("Tigre", 4)
leone = Animal("Leone", 4)

print(tigre.name)
print(leone.name)

tigre.legs = 5

tigre.setLegs(4)

Animal.printInfo(tigre)


# Exercise 4 (Folder 9 ex_4.py)
# 1. Write a new class called Food, it should have name, price and
# description as attributes.
# 2. Instantiate at least three different foods you know and like.
# 3. Create a new class called Menu, it should have a list (of Foods) as attribute.
# __init__ should take a list of Foods as optional parameters (default=[])
# 4. Create a addFood() and removeFood() for the Menu
# 5. Create a few new Food instances. Add each to the Menu using the respective
# Method.
# 6. Add a method printPrices() that list all items on the Menu with their
# prices.
# 7. Add a Menu method getAveragePrice() that returns the average Food
# price of the Menu

print("\n\n\n\nEsercizio 4\n\n")

class Food:
    
    def __init__(self, name, price, description):
        self.name = name 
        self.price = price 
        self.description = description
        
pizza = Food("Pizza", 10, "Pizza margherita")
crispy = Food("CrispyMCBacon", 8, "Best mc hamburger")
sushi = Food("Sushi", 5, "Japanese food") 

class Menu:
    
    def __init__ (self, foods = [] ):
        self.foods = foods
        
    def addFood(self, food):
        self.foods.append(food)
            
    def removeFood(self, food):
        self.foods.remove(food)
            
    def printPrices(self):
        list_prices = [] 
        for food in self.foods: 
            list_prices.append(food.price)
        
        print(list_prices)

    def getAvaragePrice(self):
        
        somma = 0
        
        for food in self.foods:
            somma += food.price
        media = somma / len(self.foods)
        print(f"La media dei prezzi è : {media }")
            
pasta = Food("Pizza", 12, "pasta with eggs and guanciale")


menu = Menu()
menu.addFood(pasta)
menu.addFood(pizza)
menu.addFood(sushi)
menu.addFood(crispy)

menu.printPrices()
menu.getAvaragePrice()