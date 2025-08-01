"""Lamda Expression
A lambda expression is a small anonymous function that can take any number of arguments but can only have one expression.
It is often used for short, throwaway functions that are not reused elsewhere in the code.
Syntax:
lambda arguments: expression
Where:  
- arguments: A comma-separated list of arguments the function takes.
- expression: A single expression that is evaluated and returned by the function.
Example:
```python
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
```
"""
x,y= 5,10
add = (lambda x, y: x + y)(3, 5)
print(add)  # Output: 15