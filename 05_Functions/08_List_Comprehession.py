"""list Compression
List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or a range) and optionally filtering items based on a condition.    
Syntax:
```python
new_list = [expression for item in iterable if condition]
```
Where:
- `new_list`: The new list being created.
- `expression`: An expression that produces the items to be included in the new list.
- `item`: A variable representing each item in the iterable.
- `iterable`: An existing iterable (like a list, tuple, or range) that you are iterating over.
- `condition` (optional): A condition that filters which items are included in the new list.
Example:
```python
# Create a list of squares of even numbers from 0 to 9
# squares = [x**2 for x in range(10) if x % 2 == 0]
# print(squares)  # Output: [0, 4, 16, 36, 64]
# # Create a list of tuples (number, square) for numbers from 0 to 4
# tuples = [(x, x**2) for x in range(5)]
# print(tuples)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
# # Create a list of characters from a string
# # chars = [char for char in "hello"]
# # print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']
# # Create a list of numbers from user input
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# squares = [x**2 for x in numbers if x % 2 == 0]
# print(squares)  # Output: squares of even numbers from user input
# # Create a list of squares of even numbers from 0 to 9 using a lambda function
squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
# print(squares)  # Output: [0, 4, 16, 36, 64]
# # Create a list of squares of even numbers from 0 to 9 using a nested list comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]
# # Create a list of squares of even numbers from 0 to 9 using a nested for loop
# squares = []  
# for x in range(10):
#     if x % 2 == 0:
#         squares.append(x**2)
# print(squares)  # Output: [0, 4, 16, 36, 64]
# # Create a list of squares of even numbers from 0 to 9 using a generator expression
# squares = (x**2 for x in range(10) if x % 2 == 0)
# print(list(squares))  # Output: [0, 4, 16, 36, 64]
# # Create a list of squares of even numbers from 0 to 9 using a list comprehension with a condition
squares = [x**2 for x in range(10) if x % 2 == 0]
# """
"""Lamda expression in list comprehension
# Lambda expressions can be used within list comprehensions to create concise, anonymous functions for transforming or filtering data.
# Syntax:
# ```python
# new_list = [lambda x: expression for item in iterable if condition]
# Where:
# - `new_list`: The new list being created.
# - `lambda x: expression`: A lambda function that takes an argument `x` and returns the result of the expression.
# - `item`: A variable representing each item in the iterable.
# - `iterable`: An existing iterable (like a list, tuple, or range) that you are iterating over.
# - `condition` (optional): A condition that filters which items are included in the new list.
# Example:
# ```python
# # Create a list of squares of even numbers from 0 to 9 using a lambda function
# squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
# # print(squares)  # Output: [0, 4, 16, 36, 64]
# # # Create a list of squares of even numbers from 0 to 9 using a nested list comprehension
"""
squares = [lambda x:x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [<function <listcomp>.<lambda> at 0x...>, <function <listcomp>.<lambda> at 0x...>, ...]