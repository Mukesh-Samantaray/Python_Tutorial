"""
Q) What is type casting in python ?
Type casting in pyhton is the process of converting the data type of a variable to anaother data type
It is used to ensure that the data is in the correct format for operations or functions that require specific data types.  
 Use Case:
1. **User Input**: When taking input from users, it is often in string format. Type casting is used to convert it to the desired type (e.g., int, float).
2. **Mathematical Operations**: When performing calculations, you may need to convert strings or other types to numeric types (e.g., int, float).
3. **Data Manipulation**: When working with data structures like lists or dictionaries, you may need to convert types for proper manipulation.
4. **Database Operations**: When interacting with databases, type casting is often required to match the expected data types in queries.
5. **API Interactions**: When sending or receiving data from APIs, type casting may be necessary to ensure compatibility with the expected data types.
"""

"""
Q) Types Of Type casting in python
1. **Implicit Type Casting**: Python automatically converts one data type to another without explicit instruction.
   - Example: Converting an integer to a float when performing arithmetic operations.
   ```python
   x = 5
   y = 2.0
   result = x + y  # Implicitly converts x to float
   print(result)  # Output: 7.0
   ```
   
   why does inplict type casting occurs?
    - Implicit type casting occurs in Python when an operation involves mixed data types, and Python automatically converts the smaller data type to a larger one to avoid data loss.
    what is the rule of implicit type casting?
    - The rule of implicit type casting is that Python promotes smaller data types to larger ones to prevent data loss during operations. For example, when an integer and a float are involved in an operation, the integer is implicitly converted to a float.
    what is data loss?
    - Data loss refers to the situation where information is lost or altered during a conversion process, such as converting a larger data type to a smaller one. For example, converting a float to an integer may result in the loss of decimal precision.

2. **Explicit Type Casting**: The programmer manually converts one data type to another using built-in functions.
    - Example: Converting a string to an integer using the `int()` function.
    ```python
    x = "10"
    y = int(x)  # Explicitly converts string to integer
    print(y)  # Output: 10
    ```
3. **Type Casting Functions**: Python provides built-in functions for type casting, including:
- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a float.
- `str()`: Converts a value to a string.
#
# Example of Type Casting Functions:
#
# ```python
# x = 10.5
# y = int(x)  # Converts float to integer
# print(y)  # Output: 10
#
# z = str(y)  # Converts integer to string
# print(z)  # Output: "10"
#
# a = "20"  
# b = float(a)  # Converts string to float
# print(b)  # Output: 20.0
#
# ```
 a=10
 b=float(a,3) # Converts integer to float"""


# x=10
# y=20.5
# print(x+y) # 30.5  
# 
# x='rabi'
# int(x) # TypeError: invalid literal for int() with base 10: 'rabi'
#why?
# The error occurs because the string 'rabi' cannot be converted to an integer.
# The `int()` function expects a string that represents a valid numeric literal

# a=10
# b=float(a)
#if i want to convert it to 3 decimal places
# b=round(b,3)
# print(b) # 10.0
#
# The `round()` function is used to round a floating-point number to a specified number of decimal places.  

b=round(10.0054,2)
print(b) # 10.0