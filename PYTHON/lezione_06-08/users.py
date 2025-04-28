# 9-11. Imported Admin: Create a module users.py containing three classes:

# User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
# Privileges: holds a list of privileges and a method show_privileges() to display them.
# Admin: stores a User instance and a Privileges instance as attributes.

class User:
    
    def __init__(self, first_name, last_name, username, email):
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        
    def __str__(self):
        
        return f"Nome: {self.first_name} Cognome: {self.last_name} Username: {self.username} Email: {self.email}"
    
    
class Privileges: 
    
    def __init__(self, *args):
        
        self.privileges = args
    
    def show_privileges(self):
        
        print(self.privleges)
    
class Admin: 
    
    def __init__(self, user, privileges):
        
        self.user = user
        self.privileges = privileges

    def describe_user(self):
        
        self.describe_user()
        
    def show_privileges(self):
        
        self.show_privileges()
