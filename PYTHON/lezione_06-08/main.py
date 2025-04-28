# In a separate file main.py, import the classes, create a User and a Privileges instance, 
# pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.

from users import Admin, User, Privileges

user1 = User("Alessandro", "Colella", "ErColle", "alessandrocolell@gmail.com")

privileges = Privileges("Add", "Delete", "Modify")

adminnn = Admin(user1, privileges)

adminnn.describe_user()