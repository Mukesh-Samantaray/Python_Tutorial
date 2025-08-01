"""Higher-Order Functions 
Higher-order functions are functions that can take other functions as arguments or return them as results.
They are a key feature of functional programming and allow for more abstract and flexible code design.
# Example:
# ```python
# 
# 
# 
# """


"""DECORATOR
A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
It is often used to add functionality to existing functions or methods in a clean and readable way.
Syntax:
```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Add functionality before calling the original function
        result = original_function(*args, **kwargs)
        # Add functionality after calling the original function
        return result
    return wrapper_function 
    ```
    Where:
    - `decorator_function`: The function that takes the original function as an argument.
    - `original_function`: The function being decorated.
    - `wrapper_function`: The inner function that adds functionality before and/or after calling the original function.
    Example:
    ```python
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result
        return wrapper
        @my_decorator
        def say_hello(name):
            print(f"Hello, {name}!")
            say_hello("Alice")  
            # Output:
            # # Something is happening before the function is called.
            # Hello, Alice!
            # # Something is happening after the function is called.
            # ```
            # Decorators can also take arguments, allowing for more flexible and reusable functionality.
            #   
            # Decorators are commonly used for:
            # - Logging function calls
            # - Timing function execution
            # - Access control and authentication
            # - Caching results"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper
@my_decorator
def say_hello(name):
        print(f"Hello, {name}!") 
say_hello("Alice")
 # Output: wrapper       

#logging function calls example
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
@log_function_call
def add(a, b):
    return a + b    
@log_function_call
def multiply(a, b):
    return a * b
add(3, 5)
multiply(4, 6)
# Output:

def Decorator(func):
    print(f"{func.__name__} is not decorated yet")
    def Wrapper(*args,**kwargs):
         print(f"")
# 