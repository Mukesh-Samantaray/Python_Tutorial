""" integer data type
The integer data type is a built-in data type in Python that represents whole numbers, both positive and negative, without any decimal points.
 Integers can be of arbitrary size, meaning they can be as large or as small as the memory allows. 
 In Python, integers are represented using the int class.


"""
# # Example of integer data type
# a=5
# b=-3
# c=0
# print("a:",a,type(a))
# # The type() function returns the type of the object passed to it.
# # In this case, it returns <class 'int'>, indicating that the variable a is of type int.
# # The int class is used to represent integer values in Python.
# print("b:",b,type(b))
# print("c:",c,type(c))

'''--------------------------------------------'''
""""How does pyhton know that a number is an integer or not?
# Python uses the int class to represent integer values.
# The int class is a built-in class in Python that provides methods and attributes for working with integer values.
"""
"""conversion of different type
# Python provides several built-in functions for converting between different data types.
# The most common conversion functions are:
# 1. int(): Converts a value to an integer.
# 2. float(): Converts a value to a floating-point number.
# 3. str(): Converts a value to a string.
# 4. list(): Converts a value to a list.
# 5. tuple(): Converts a value to a tuple.
# 6. set(): Converts a value to a set.
# 7. dict(): Converts a value to a dictionary.
# 8. bool(): Converts a value to a boolean.
# 9. complex(): Converts a value to a complex number.
# 10. bytes(): Converts a value to a bytes object.
# 11. bytearray(): Converts a value to a bytearray object.
# 12. memoryview(): Converts a value to a memoryview object.
# 13. frozenset(): Converts a value to a frozenset object.
# 14. range(): Converts a value to a range object."""



"""How to convert a string to an integer"""
# Python provides the int() function to convert a string to an integer.
# The int() function takes a string as an argument and returns the integer value of the string.
# The string must represent a valid integer value, otherwise a ValueError will be raised.
# # Example:
# str_num = "123"
# int_num = int(str_num)
# print(int_num, type(int_num))

'''the string must represent a valid integer value, otherwise a ValueError will be raised.'''
# # Example:
# str_num = "123abc"
# int_num = int(str_num)
# print(int_num, type(int_num))
# # Output:
# # ValueError: invalid literal for int() with base 10: '123abc'
'''It Can be handled using isdigit() method'''
# # Example:
'''---------------------------------------------'''
# str_num =input("Enter a number: ")
# if str_num is not None:
#   if str_num.isdigit():
#     int_num = int(str_num)
#     print(int_num, type(int_num))
#   else: 
#     print("Invalid input: not a valid integer string")
# print("You have not entered anything")

'''The int() function can also take a second argument, which specifies the base of the number system to use for conversion.'''
# # Example:
# str_num = "1010"
# int_num = int(str_num, 2) # Convert binary string to integer
# print(int_num, type(int_num))
# # Output:
# # 10 <class 'int'>
''' convert binary string to integer'''
# a="109"
# print(int(a,base=16))# we can write only 2,8,10,16
""" convert integer to binary string"""
# Python provides the bin() function to convert an integer to a binary string.
# The bin() function takes an integer as an argument and returns the binary string representation of the integer.
# Example:
num = 10
binary_str = bin(num)   
# Remove the '0b' prefix
binary_str = binary_str[2:]

print(type(binary_str),binary_str)
