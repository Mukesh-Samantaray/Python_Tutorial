"""
Flow Control - If-Else Statements
In Python, if-else statements are used to execute a block of code based on a condition.
The syntax is as follows:
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
elif condition:
    # code to execute if condition is true
else:
    # code to execute if all conditions are false
Example:
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")   
example with multiple conditions:
age = 18
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
"""

# We can also write if statements in a single line using the ternary operator
# Syntax: value_if_true if condition else value_if_false
# age = 18
# result="adult "if age>= 18 else "Minor"
# print(result)
# print("You Can watch Netflix") if age>=18 else print("You can't watch Netflix")
# Example with multiple conditions
# age = 18
# if age>0 and age<13:
#     print("You are a child.")
# elif age>=13 and age<18:
#     print("You are a teenager.")