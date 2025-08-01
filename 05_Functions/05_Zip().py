"""Zip()
The zip() function in Python is used to combine two or more iterables (like lists or tuples) into a single iterable of tuples. Each tuple contains elements from the input iterables that are at the same index.
Syntax:
zip(iterable1, iterable2, ...)
Where:  
- iterable1, iterable2, ...: The iterables to be combined. They can be of different lengths, but the resulting iterable will be as long as the shortest input iterable.
Example:
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```
Using zip() with different lengths:
```python
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b')]
```
Using zip() with more than two iterables:
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print(list(zipped))  # Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
```
Using zip() with unpacking:
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(*zip(list1, list2))
print(list(zipped))  # Output: [(1, 2, 3), ('a', 'b', 'c')]
``` 
Using zip() with dictionaries:
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'x': 10, 'y': 20}
zipped = zip(dict1.items(), dict2.items())
print(list(zipped))  # Output: [(('a', 1), ('x', 10)), (('b', 2), ('y', 20))]
``` 
Using zip() with user input:
```python
list1 = list(map(int, input("Enter numbers for list1 separated by space: ").split()))
list2 = input("Enter characters for list2 separated by space: ").split()
zipped = zip(list1, list2)
print(list(zipped))  # Output: Pairs of numbers and characters from user input
``` 
"""
"""Unzipping with zip():
To unzip a list of tuples, you can use the zip() function with the unpacking operator *:
```python

"""
# zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
# print(list(zip(*zipped)))