"""
Arithmetic Operators
Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, division, and more.
They are commonly used in programming to manipulate numerical data and perform calculations.    


The following are the most common arithmetic operators in Python:
1. **Addition (`+`)**: Adds two numbers together.
2. **Subtraction (`-`)**: Subtracts one number from another.
3. **Multiplication (`*`)**: Multiplies two numbers together.
4. **Division (`/`)**: Divides one number by another and returns a float.
5. **Floor Division (`//`)**: Divides one number by another and returns the largest integer less than or equal to the result.
6. **Modulus (`%`)**: Returns the remainder of the division of one number by another. #Python Modulos operator retuns the remainder as the sign of dividend
7. **Exponentiation (`**`)**: Raises one number to the power of another.
8. **Unary Negation (`-`)**: Negates a number (changes its sign).
9. **Unary Plus (`+`)**: Indicates a positive number (usually optional).
10. **Augmented Assignment Operators**: These operators combine arithmetic operations with assignment. For example, `+=` adds a value to a variable and assigns the result back to that variable.
11. **Operator Precedence**: Arithmetic operators follow a specific order of precedence when evaluating expressions. For example, multiplication and division are performed before addition and subtraction.
12. **Associativity**: When multiple operators of the same precedence appear in an expression, they are evaluated from left to right (or right to left for exponentiation).
13. **Type Conversion**: When performing arithmetic operations with different data types (e.g., integers and floats), Python automatically converts the operands to a common type to ensure accurate calculations.  
14. **Complex Numbers**: Python supports complex numbers, which can be represented using the `j` suffix (e.g., `3 + 4j`). Arithmetic operations can be performed on complex numbers as well.
15. **Precision**: Python's floating-point arithmetic may introduce small rounding errors due to the way numbers are represented in memory. 
    To mitigate this, you can use the `round()` function to control the number of decimal places in the result. 
16. **Order of Operations**: Parentheses can be used to group expressions and control the order of evaluation. For example, `(2 + 3) * 4` evaluates to `20`, while `2 + 3 * 4` evaluates to `14`.   

"""
'''
# Example of Arithmetic Operators
a = 10
b = 3
# Addition
addition = a + b
# Subtraction
subtraction = a - b
# Multiplication
multiplication = a * b
# Division
division = a / b
# Floor Division
floor_division = a // b                      floor division rounds down (toward negative infinity).
# Modulus
modulus = a % b                            #Python Modulos operator retuns the remainder as the sign of dividend
# Exponentiation
exponentiation = a ** b
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division.__round__(2))    
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

# Example of Unary Negation
x = 5
y = -x
print("Unary Negation:", y)  # Output: -5
# Example of Unary Plus
z = +x
print("Unary Plus:", z)  # Output: 5
# Example of Augmented Assignment Operators
x += 2  # Equivalent to x = x + 2
print("Augmented Assignment (x += 2):", x)  # Output: 7
# Example of Operator Precedence
result = 2 + 3 * 4
print("Operator Precedence (2 + 3 * 4):", result)  # Output: 14 
# Example of Type Conversion
int_num = 5
float_num = 2.5
result = int_num + float_num
print("Type Conversion (int + float):", result)  # Output: 7.5
# Example of Complex Numbers
complex_num = 3 + 4j
print("Complex Number:", complex_num)  # Output: (3+4j)
# Example of Precision
float_num = 1.23456789
rounded_num = round(float_num, 2)
print("Rounded Number:", rounded_num)  # Output: 1.23
# Example of Order of Operations
result = (2 + 3) * 4
print("Order of Operations ((2 + 3) * 4):", result)  # Output: 20



# Example of Division by Zero
try:
    division_by_zero = a / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# Example of Division by Zero with Floor Division
try:
    floor_division_by_zero = a // 0 
except ZeroDivisionError:
    print("Error: Floor division by zero is not allowed.")
# Example of Division by Zero with Modulus
try:
    modulus_by_zero = a % 0
except ZeroDivisionError:
    print("Error: Modulus by zero is not allowed.")
# Example of Division by Zero with Exponentiation
try:
    exponentiation_by_zero = a ** 0
except ZeroDivisionError:
    print("Error: Exponentiation by zero is not allowed.")


'''
"""
#Python Modulos operator retuns the remainder as the sign of dividend
#a % b = a - b * (a // b) it is used to find the remainder of a division operation.
a=10
b=3
print(a%b) # 1
print(-a%b) # 2
print(a%-b) # -2
print(-a%-b) # -1
print(a//b) # 3
print(-a//b) # -4
print(a//-b) # -4
print(-a//-b) # 3
print(a/b) # 3.3333333333333335
print(-a/b) # -3.3333333333333335
print(a/-b) # -3.3333333333333335
print(-a/-b) # 3.3333333333333335
print(a**b) # 1000
print(-a**b) # -1000
print(a**-b) # 0.001
"""
"""
Here’s the order of precedence (from highest to lowest) in Python arithmetic operations:

() → Parentheses (for grouping)

** → Exponentiation

+x, -x, ~x → Unary plus, minus, and bitwise NOT

*, /, //, % → Multiplication, Division, Floor Division, Modulus

+, - → Addition and Subtraction

<<, >> → Bitwise shifts

& → Bitwise AND

^ → Bitwise XOR

| → Bitwise OR


"""
# Example 
result=(2 + 3) * 4
print("Order of Operations ((2 + 3) * 4):", result)  # Output: 20
## Complex Calculation
a = 10
b = 5
c = 2
d = 3
result = a + b * c - d / 2 ** 3
print("Complex Calculation Result:", result)  # Output: 10 + 5 * 2 - 3 / 8 = 19.625