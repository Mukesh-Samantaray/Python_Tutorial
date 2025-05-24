"""
Overview of Sets in Python

A set is an unordered collection of unique and immutable elements. Sets are useful for membership testing, removing duplicates, and performing mathematical set operations like union, intersection, difference, and symmetric difference.

Key Features:
- Unordered: No indexing or slicing.
- Unique elements: Duplicates are automatically removed.
- Mutable: You can add or remove elements.
- Elements must be immutable (e.g., numbers, strings, tuples).

Common Operations:
- Creation: Use curly braces `{}` or the `set()` constructor.
- Adding: Use `add()` to insert a single element.
- Removing: Use `remove()` (raises error if not found) or `discard()` (no error if not found).
- Set operations: Use `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference).
- Membership: Use `in` to check if an element exists.
- Iteration: Use a for loop to iterate over elements.

Sets are commonly used for tasks like deduplication, fast membership tests, and mathematical set operations.

''' all()	Returns True if all elements of the set are true (or if the set is empty).
any()	Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()	Returns the length (the number of items) in the set.
max()	Returns the largest item in the set.
min()	Returns the smallest item in the set.
sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
sum()	Returns the sum of all elements in the set.
"""
# my_set = {0, 1, 2, 3}

# print("Set:", my_set)

# print("all():", all(my_set))             # False because 0 is falsy
# print("any():", any(my_set))             # True because 1, 2, 3 are truthy
# print("enumerate():")
# for i, val in enumerate(my_set):
#     print(f"  Index {i}: Value {val}")

# print("len():", len(my_set))             # 4
# print("max():", max(my_set))             # 3
# print("min():", min(my_set))             # 0
# print("sorted():", sorted(my_set))       # [0, 1, 2, 3]
# print("sum():", sum(my_set))             # 6
"""
'''

Advanced Set Methods:
- `update(iterable)`: Adds multiple elements from an iterable.
- `pop()`: Removes and returns an arbitrary element.
- `clear()`: Removes all elements from the set.
- `copy()`: Returns a shallow copy of the set.
- `issubset(other)`: Checks if set is a subset of another.
- `issuperset(other)`: Checks if set is a superset of another.
- `isdisjoint(other)`: Checks if sets have no elements in common.

Note: Sets cannot contain mutable types like lists or other sets, but can contain tuples if the tuples themselves only contain immutable elements.
"""
# # Creating sets
# my_set = {1, 2, 3}
# another_set = set([1, 2, 3, 2])  # duplicates are removed

# # Adding elements
# my_set.add(4)

# # Removing elements
# my_set.remove(2)      # Raises KeyError if not found
# my_set.discard(5)     # Does nothing if not found

# # Set operations
# a = {1, 2, 3}
# b = {3, 4, 5}
# union = a | b         # {1, 2, 3, 4, 5}
# intersection = a & b  # {3}
# difference = a - b    # {1, 2}
# symmetric_diff = a ^ b # {1, 2, 4, 5}

# # Membership test
# 3 in my_set           # True or False

# # Iterating
# for item in my_set:
#     print(item)
"""Lets Practice"""
# Mset={1,3,4,5,5}
# print(Mset) #---------------- duplicates are automatically removed


# Mset=set([1,"ab","_"])
# print(Mset)              #---Set can contain multiple data type elements 

# Mset=set("Mukesh Samantaray")#---- REMEMBER IT TAKES ONLY ITERABLE OBJECTS
# print(Mset) #--- give set of string characters in unordered manner


"""Addition In set"""

# Mset={3,4,5,6}
# Mset.add("Mango")#--- add element but not in specific position
# print(Mset)

# mset={1,2,3,4}

# mset.update("str")#----- when you want to  add items from iterable,it will add randomly
# print(mset)
"""Deletion In Set"""
# m={1,4,2,4}
# # print(m.remove(6))#---- It will raise key error if the element is not found in the set
# print(m.remove(4))
# print(m)


# m=set("Mukesh")
# m.remove("M")
# print(m)


# m={3,467,456}
# print(m.discard(3))#----- It Returns none and discard given element from the set
# print(m)
# print(m.discard(7))#----- It Returns none and discard given element from the set and does not make error
# print(m)
""" Necesarry operations  """
# m=set(1)
# print(m) #Error set takes only iterable

# m=set(range(1,5))
# print(m)


# m={2,4,5}
# print(enumerate(m))
# y=set(enumerate(m))#---- give index
# print(y)

# m={2,4,5,67}
# print(sorted(m),id(m),id(sorted(m))) #----- returns  new list with sorted elements

# print(sorted(["And","Or"])) #--- It use leximographic to sort the value 




# m.pop(5)#--- in set .pop() takes no argument
# print(m)

# m.pop()
# print(m)

""""""
# Mset={["Mango","Orange"]}
# print(Mset) #---- Throw Unhashable type set error, as set can not contain mutable elements

# Mset={[1]}
# print(Mset)"""
""" Here The Concept of Frozen set is Come"""
# # List
# print(frozenset([1, 2, 3]))       # ✅ frozenset({1, 2, 3})

# # Tuple
# print(frozenset((4, 5, 6)))       # ✅ frozenset({4, 5, 6})

# # Set
# print(frozenset({7, 8}))          # ✅ frozenset({8, 7})

# # String
# print(frozenset("abc"))           # ✅ frozenset({'a', 'b', 'c'})

# # Range
# print(frozenset(range(3)))        # ✅ frozenset({0, 1, 2})

# # Frozen Set Example
# # A frozenset is an immutable version of a set. Its elements cannot be changed after creation.
# fset = frozenset([1, 2, 3, 4])
# print(fset)  # Output: frozenset({1, 2, 3, 4})

# # You can use frozenset as an element of another set, since it is immutable and hashable.
# Mset = {frozenset([1, 2]), frozenset([3, 4])}
# print(Mset)

"""
Interview Information:

Q: What is a frozenset in Python?
A: A frozenset is an immutable and hashable version of a set. Once created, its elements cannot be changed, added, or removed. This makes frozenset suitable for use as dictionary keys or as elements of other sets.

Q: When would you use a frozenset instead of a set?
A: Use a frozenset when you need a set-like collection that must not change during its lifetime, or when you need to use a set as a key in a dictionary or as an element in another set.

Q: Can you add or remove elements from a frozenset?
A: No, frozensets are immutable. You cannot add or remove elements after creation.

Q: Can a set contain another set as an element?
A: No, because sets are mutable and unhashable. However, a set can contain a frozenset, since frozensets are immutable and hashable.

Q: What are some common use cases for frozenset?
A: Frozensets are useful for representing constant sets, as keys in dictionaries, as elements in other sets, and for ensuring that a set of items does not change accidentally.

Coding Questions:

Q: How do you create a frozenset from a list?
A: 
lst = [1, 2, 3]
fset = frozenset(lst)
print(fset)

Q: How do you check if a frozenset is a subset of another set?
A:
a = frozenset([1, 2])
b = {1, 2, 3}
print(a.issubset(b))

Q: Can you use a frozenset as a key in a dictionary? Show an example.
A:
d = {frozenset([1, 2]): "value"}
print(d)

Q: What happens if you try to add an element to a frozenset?
A:
fset = frozenset([1, 2])
# fset.add(3)  # This will raise an AttributeError

Q: How do you perform union and intersection with frozensets?
A:
a = frozenset([1, 2])
b = frozenset([2, 3])
print(a | b)  # Union
print(a & b)  # Intersection
"""

"""
# Shallow vs Deep Copy in Python

# Shallow Copy:
# Copies the outer object, but not the nested objects. Changes to nested objects affect both copies.
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99

print("Original after shallow copy modification:", original)  # [[99, 2], [3, 4]]
print("Shallow copy:", shallow)   # [[99, 2], [3, 4]]

# Deep Copy:
# Copies the outer object and all nested objects recursively. Changes to nested objects do not affect the original.
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 88

print("Original after deep copy modification:", original)  # [[1, 2], [3, 4]]
print("Deep copy:", deep)   # [[88, 2], [3, 4]]

# Real-world use cases:
# Shallow copy is useful when you want a new container but shared nested objects (e.g., configuration templates).
# Deep copy is needed when you want to fully duplicate complex objects (e.g., duplicating a game state, undo/redo functionality).

"""
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

# shallow[0][0] = 99

print(original)  # [[99, 2], [3, 4]]
print(shallow)   # [[99, 2], [3, 4]]

