"""Filter()
The filter() function constructs an iterator from elements of an iterable for which a function returns true.
It is commonly used to filter data based on a condition.
Syntax:
filter(function, iterable)
Where:
- function: A function that tests whether each element of the iterable is true or false. If None, it simply filters out false values.
- iterable: An iterable (like a list, tuple, or string) whose items will be processed by the function.
Example:
```python
def is_even(x):
    return x % 2 == 0
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = filter(is_even, numbers)
    print(list(even_numbers))  # Output: [2, 4, 6]"""
"""It stores the element which returns true"""


"""Difference between map and filter"""
# map applies a function to each item in an iterable and returns a new iterable with the results.
# filter applies a function to each item in an iterable and returns a new iterable containing only the items for which the function returned true.
def is_even(x):
    return x % 2 == 0
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
squared_even_numbers = map(square, even_numbers)
even_numbers = filter(is_even, numbers)
even_numbers = filter(is_even, numbers)
print(list(squared_even_numbers),list(even_numbers))  # Output: [4, 16, 36]
# # Example with user input
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# even_numbers = filter(is_even, numbers)
# squared_even_numbers = map(square, even_numbers)
# print(list(squared_even_numbers))  # Output: squared values of even numbers from input
# # Example with lambda function
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# squared_even_numbers = map(lambda x: x * x, even_numbers)
# print(list(squared_even_numbers))  # Output: [4, 16, 36]
# # Example with multiple iterables
# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# summed_numbers = filter(lambda x: x > 5, map(lambda x, y: x + y, numbers1, numbers2))
# print(list(summed_numbers))  # Output: [7, 8, 9]
