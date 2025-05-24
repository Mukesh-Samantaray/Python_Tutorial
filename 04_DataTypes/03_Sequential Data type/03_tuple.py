"""tuple"""
"""
This module provides an overview of the tuple data type in Python.

A tuple is an immutable, ordered sequence of elements. Tuples can contain elements of different data types and support indexing, slicing, and iteration. They are commonly used to group related data and can be used as keys in dictionaries due to their immutability.

Example:
    my_tuple = (1, "apple", 3.14)

Key Features:
- Immutable: Tuples cannot be modified after creation.
- Ordered: Elements maintain their insertion order.
- Allow duplicate values.
- Can contain heterogeneous data types.

Use cases:
- Returning multiple values from a function.
- Storing data that should not change.
- Using as keys in dictionaries or elements in sets.
"""
# Example usage of tuples

# Creating a tuple
# my_tuple = (1, "apple", 3.14)
# print("my_tuple:", my_tuple)

# # Accessing elements
# print("First element:", my_tuple[0])

# # Slicing
# print("Slice:", my_tuple[1:])

# # Iterating over a tuple
# for item in my_tuple:
#     print("Item:", item)

# # Tuple unpacking
# a, b, c = my_tuple
# print("Unpacked:", a, b, c)

# # Tuples as dictionary keys
# my_dict = {my_tuple: "example value"}
# print("Dictionary with tuple key:", my_dict)

#print unique element from a tuple
a=(1,2,3,3,4,5)
print(set(a))
