# Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
# Handle ValueError if the input is negative by returning an informative message.

def safe_sqrt(number):
    try:
        import math
        return math.sqrt(number)
    except ValueError:
        return "Cannot calculate the square root of a negative number."
    
print(safe_sqrt(-10))

# Password Validation 1:  Write a function validate_password(password) that checks whether a password meets the following criteria:
# Minimum length of 20 characters, At least three uppercase letters, At least four special characters (non-alphanumeric). 
# If the password is valid, the function should return True. 
# If the password is invalid, the function should raise a built-in exception (e.g., ValueError) 
# with a message indicating which criteria were not met.

class CustomError(Exception):
    if self
