
"""
 Input () Always Returns a String
"""
"""
input() : function to take input from the user
input(prompt) : function to take input from the user with a prompt message
input () always returns a string
input() function is used to take input from the user in Python.
It reads a line from the input, converts it into a string (stripping a trailing newline), and returns it.
The input() function can take an optional prompt string as an argument, which is displayed to the user before taking input.
The input() function is commonly used for interactive programs where user input is required.

"""


# Age=input("Enter Your age:")
# print("Your age is:",Age)
# # The input() function always returns a string, even if the user enters a number.
# print(type(Age))  # Output: <class 'str'>
# # To convert the input to an integer, you can use type casting: 
# Age=int(Age)
# print("Your age is:",Age)
# print(type(Age))  # Output: <class 'int'>

"""
String Formatting
String formatting is the process of creating a string by inserting values into placeholders within a string template.
It allows you to create dynamic strings by combining text and variables.
There are several ways to format strings in Python, including:
1. **f-strings (formatted string literals)**: Introduced in Python 3.6, f-strings allow you to embed expressions inside string literals using curly braces `{}`.
   ```python
   name = "Alice"
   age = 25
   formatted_string = f"My name is {name} and I am {age} years old."
   print(formatted_string)
   ```
2. **str.format() method**: This method allows you to format strings by using curly braces `{}` as placeholders and calling the `format()` method on the string.
   ```python
    name = "Alice"
    age = 25
    formatted_string = "My name is {} and I am {} years old.".format(name, age)
3. **Old-style formatting**: This method uses the `%` operator to format strings, similar to the `printf` function in C.
    ```python
    name = "Alice"
    age = 25
    formatted_string = "My name is %s and I am %d years old." % (name, age)
    print(formatted_string)
    ```
    """
# Name="Mukesh"
# Age=25
# print(f"My name is {Name} and I Am {Age} years old")
# print("Name {} and age {}".format(Name,Age))
# print("Name {0} and age {1}".format(Name,Age))
# print("Name %s and age %d" % (Name,Age))


# # mixed arguments
# print("Hello {0}, your balance is {1}.".format( "Mukesh",blc=230.2346))
print("Hello {0}, your balance is {1}.".format( "Mukesh",230.2346))
