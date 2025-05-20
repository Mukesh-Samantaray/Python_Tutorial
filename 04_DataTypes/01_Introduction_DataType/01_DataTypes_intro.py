"""
Data Types in Python
What are Data Types?
Python has several built-in data types that are used to store different types of data. The most common data types in Python are:
1. Numeric Types: These include integers (int), floating-point numbers (float), and complex numbers (complex).
2. Sequence Types: These include strings (str), lists, tuples, and ranges.
3. Mapping Type: This includes dictionaries (dict).
4. Set Types: These include sets and frozensets.
5. Boolean Type: This includes boolean values (bool).
6. Binary Types: These include bytes, bytearray, and memoryview.
7. None Type: This includes the None value, which represents the absence of a value.
8. Callable Types: These include functions and methods.
1. Integers (int): Whole numbers, both positive and negative, without decimals. Example: 5, -3, 0
2. Floating-point numbers (float): Numbers with decimal points. Example: 3.14, -0.001, 2.0
3. Strings (str): A sequence of characters enclosed in single or double quotes. Example: "Hello, World!", 'Python'
4. Lists: An ordered collection of items, which can be of different data types. Lists are mutable (can be changed). Example: [1, 2, 3], ['apple', 'banana', 'cherry']
5. Tuples: An ordered collection of items, which can be of different data types. Tuples are immutable (cannot be changed). Example: (1, 2, 3), ('apple', 'banana', 'cherry')
6. Dictionaries: A collection of key-value pairs, where each key is unique. Dictionaries are mutable. Example: {'name': 'Alice', 'age': 25}
7. Sets: An unordered collection of unique items. Sets are mutable. Example: {1, 2, 3}, {'apple', 'banana', 'cherry'}
8. Booleans (bool): Represents one of two values: True or False. Example: True, False
9. None: Represents the absence of a value or a null value. Example: None
10. Bytes: A sequence of bytes, used to represent binary data. Example: b'hello', b'\x00\x01\x02'
11. Bytearray: A mutable sequence of bytes. Example: bytearray(b'hello'), bytearray([0, 1, 2])
12. Memoryview: A memory view object that allows you to access the internal data of an object that supports the buffer protocol without copying it. Example: memoryview(b'hello'), memoryview(bytearray([0, 1, 2]))
13. Frozenset: An immutable version of a set. Example: frozenset([1, 2, 3]), frozenset({'apple', 'banana', 'cherry'})
14. Complex numbers: Numbers with a real and imaginary part. Example: 3 + 4j, -2 - 3j
15. Range: A sequence of numbers, commonly used in for loops. Example: range(5), range(1, 10, 2)
16. Type: A built-in function that returns the type of an object. Example: type(5), type("Hello")
17. Object: The base class for all classes in Python. All classes in Python inherit from the object class.
18. Callable: An object that can be called as a function. Example: def func(): pass, lambda x: x + 1
19. Iterator: An object that implements the iterator protocol, which consists of the __iter__() and __next__() methods. Example: iter([1, 2, 3]), iter("hello")
20. Generator: A special type of iterator that is defined using a function with the yield statement. Example: def gen(): yield 1; yield 2; yield 3
21. Coroutine: A special type of generator that can be paused and resumed. Example: async def coro(): await asyncio.sleep(1)
22. Asyncio: A library for writing concurrent code using the async/await syntax. Example: async def main(): await asyncio.sleep(1)
23. Context manager: An object that defines the runtime context to be established when executing a with statement. Example: with open('file.txt', 'r') as f: pass


"""