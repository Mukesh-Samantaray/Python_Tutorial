"""
Fulll Overview of Class and object in python including interview questions

A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
An object is an instance of a class. It contains data and methods defined by the class.
Setting up a class and creating objects allows for encapsulation, inheritance, and polymorphism in Python.
# Overview of Classes and Objects in Python
#
# A class is a blueprint for creating objects, encapsulating data and behavior.
# An object is created to access the class's attributes and methods.

#
# Key Concepts:
# - Class: A template for creating objects, defining attributes and methods.
# - Object: An instance of a class, containing specific data.
# - Attributes: Variables that hold data for the class.
# - Methods: Functions defined within a class that operate on the object's data.
# - Constructor: A special method `__init__` that initializes an object when created.
# - Inheritance: A way to create a new class based on an existing class, inheriting its attributes and methods.
# - Polymorphism: The ability to use a single interface to represent different data types.
#
# Class Definition:

class ClassName:
    def __init__(self, attribute1, attribute2):
    #    Constructor to initialize object attributes.
        self.attribute1 = attribute1  # Instance variable
        self.attribute2 = attribute2  # Instance variable

    def method_name(self, parameter):
        # A method that performs an action.
        print(f"Method called with {parameter}")
#
# Creating an Object:
# object_name = ClassName(value1, value2)
# object_name = ClassName("value1", "value2")
#
# Accessing Attributes and Methods:
# object_name.attribute1  # Accessing an attribute
# object_name.method_name(argument)  # Calling a method
#
# Example:
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# Creating an object of the Person class

person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.


"""
# class q:
#     a=20
#     print(a)
# object=q()    
"Here We can access the class members without creating an object then What is the need of creating an object?"
"""
    # Answer: 
    # - Creating an object allows for encapsulation, where data and methods are bundled together.
    # - Objects can have unique states (attributes) and behaviors (methods).
    # - It enables polymorphism and inheritance, allowing for more complex and reusable code.
    # - Objects can maintain their own state, while class variables are shared across all instances.
    """

    # # Example of accessing class members without creating an object 
    # print(A.a)  # Output: 20
    # # Accessing class members using the class name
    # print(A.__dict__)  # Output: {'__module__': '__main__', 'a': 20, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
    # # Accessing class members using the class name
    # print(A.__name__)  # Output: A
    # # Accessing class members using the class name
    # print(A.__module__)  # Output: __main__
    # # Accessing class members using the class name
    # print(A.__bases__)  # Output: (<class 'object'>,)
    # define a class
