"""Map()
The map() function applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
It is often used for transforming data in a functional programming style.
Syntax:
map(function, iterable, ...)
Where:
- function: A function that takes one or more arguments and returns a value.
- iterable: An iterable (like a list, tuple, or string) whose items will be processed by the function.
- ...: Additional iterables can be passed if the function takes multiple arguments.
Example:
```python
def square(x):
    return x * x
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(square, numbers)
    print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
    def add(x, y):
        return x + y
        numbers1 = [1, 2, 3]
        numbers2 = [4, 5, 6]
        summed_numbers = map(add, numbers1, numbers2)
        print(summed_numbers*)  # Output: [5, 7, 9]
"""
"""
How Map is used while taking input from user
def square(x):
    return x * x
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    squared_numbers = map(square, numbers)
    print(list(squared_numbers))  # Output: squared values of the input numbers
    """
# It is often used for transforming data in a functional programming style.
# for which purpose map is used in industry
# Map is commonly used in data processing tasks, such as:
# 1. Data Transformation: Applying a function to each element in a dataset to transform it, such as converting strings to integers or applying mathematical operations.
# 2. Data Cleaning: Removing unwanted characters or formatting data consistently.
# 3. Feature Engineering: Creating new features from existing data in machine learning pipelines.
# 4. Parallel Processing: In distributed computing, map can be used to apply a function across multiple data points in parallel.
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# we can simply call the original function with arguments then why use map
# Using map allows for cleaner and more concise code, especially when dealing with large datasets or multiple transformations.


