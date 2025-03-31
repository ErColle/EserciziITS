# In a separate file main.py, import the classes, create a User and a Privileges instance, 
# pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.

from users import User, Privileges, Admin

user1 = User("Alessandro", "Colella", "ErColle", "alessandrocolell@gmail.com")

privileges = Privileges("Add", "Delete", "Modify")

admin = Admin(user1, privileges)

admin.describe_user()
admin.show_privileges()