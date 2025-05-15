"""
  Q)What is a variable in Python?
    A variable in Python is a symbolic name that refers to a value. It acts as a container for storing data values.
    Variables are created when you assign a value to them. In Python, you don't need to declare the variable type explicitly; it is inferred from the value assigned.
    Variable names can consist of letters, digits, and underscores, but they must start with a letter or an underscore.
    Variable names are case-sensitive, meaning `myVar` and `myvar` are considered different variables.
    Python has some reserved keywords that cannot be used as variable names, such as `if`, `else`, `while`, `for`, etc.
    
            # _a=10
            # print(_a)

"""
"""
     Q)What is literal in Python?
    A literal in Python is a fixed value that is represented directly in the code.
    Literals can be of various types, including:
    1. **Numeric Literals**: Represent numbers, such as integers and floats.
       - Example: `10`, `3.14` 
    2. **String Literals**: Represent text, enclosed in single or double quotes.
    3. **Boolean Literals**: Represent truth values, either `True` or `False`.
    4. **None Literal**: Represents the absence of a value, denoted by `None`.
    5. **Collection Literals**: Represent collections of values, such as lists, tuples, sets, and dictionaries.
       - Example: `[1, 2, 3]`, `(1, 2)`, `{1, 2}`, `{'key': 'value'}`
    6. **Special Literals**: Represent special values, such as `Ellipsis` (`...`) and `NotImplemented`.



"""
"""
Various format of assigning variables
1. **Single Assignment**: Assigning a single value to a variable.
   ```python
   x = 10
   ```
2. **Multiple Assignment**: Assigning multiple values to multiple variables in a single line.
   ```python
    x, y, z = 1, 2, 3
    ```
3. **Chained Assignment**: Assigning the same value to multiple variables.
    ```python
    e.g: a = b = c = 5
    
    e.g: a=b=c=[1,2,3]
    print(a,b,c)


    ```
4. **Tuple Unpacking**: Assigning values from a tuple to multiple variables.
    ```python
    coordinates = (10, 20)
    x, y = coordinates
    ```
    coordinates = (10, 20,30)
    x, y,z = coordinates
    print(x, y,z)
   (( the variable must be delaclared in same order you want and the number of variables must be same as the number of values in the tuple.)))

5. **List Unpacking**: Assigning values from a list to multiple variables.
    ```python
    values = [1, 2, 3]
    a, b, c = values
    ```
the variable must be delaclared in same order you want and the number of variables must be same as the number of values in the list.
6. **Dictionary Unpacking**: Assigning values from a dictionary to variables using keys.
    ```python
    person = {'name': 'Alice', 'age': 25}
    name, age = person['name'], person['age']
    ```
7. **Extended Unpacking**: Using the `*` operator to capture multiple values in a list.
    ```python
    a, *b, c = [1, 2, 3, 4, 5]
    ```
    In this case, `a` will be the first element, `b` will be a list of the middle elements, and `c` will be the last element.
    ```python
    a, *b, c = [1, 2, 3, 4, 5]
    print(a, b, c)
    ```
"""
# values = [1, 2, 3]
# a, b, c = values[0], values[1], values[2]
# print(a, b, c)

# person = {'name': 'Alice', 'age': 25}
# name, age = person['name'], person['age']
# print(name, age)


# a,b,c=[1,2,3]
# print(a,b,c)


# a=b=c=[1,2,3] -- Simultaneously pointing to the same memory location
#               -- This means that if you modify one of the lists, the others will also be affected.
# print(a,b,c)

# b+=[4,5]
# print(a is b) ---- important both  are results different
# a=a+[4,5]
# print(a,b,c)


# a, *b, c = [1, 2, 3, 4, 5]
# print(a, b, c)
'''
is a comparison operator in Python that checks if two variables point to the same object in memory.
It returns True if they do, and False otherwise.
== is a comparison operator that checks if the values of two variables are equal, regardless of whether they point to the same object in memory.
id() is a built-in function that returns the unique identifier (memory address) of an object.
is internally use id() to check the memory address of the object.


'''

