"""
Comparison Operators
Comparison operators are used to compare two values or expressions.
They return a Boolean value (`True` or `False`) based on the result of the comparison.
The following are the most common comparison operators in Python:
1. **Equal to (`==`)**: Checks if two values are equal.
2. **Not equal to (`!=`)**: Checks if two values are not equal.
3. **Greater than (`>`)**: Checks if the left value is greater than the right value.
4. **Less than (`<`)**: Checks if the left value is less than the right value.
5. **Greater than or equal to (`>=`)**: Checks if the left value is greater than or equal to the right value.
6. **Less than or equal to (`<=`)**: Checks if the left value is less than or equal to the right value.
7. **Identity Operators**: These operators check if two variables point to the same object in memory. The `is` operator checks for identity, while the `is not` operator checks for non-identity.
8. **Membership Operators**: These operators check if a value is present in a sequence (e.g., list, tuple, string). The `in` operator checks for membership, while the `not in` operator checks for non-membership.
9. **Chained Comparisons**: Python allows you to chain multiple comparison operators together. For example, `a < b < c` checks if `a` is less than `b` and `b` is less than `c`.
10. **Boolean Context**: Comparison operators can be used in conditional statements (e.g., `if`, `while`) to control the flow of the program based on the result of the comparison.
11. **Short-Circuit Evaluation**: In logical expressions, Python uses short-circuit evaluation, meaning it stops evaluating as soon as the result is determined. For example, in `a and b`, if `a` is `False`, `b` is not evaluated.
12. **Type Comparison**: You can use the `type()` function to compare the types of two variables. For example, `type(a) is int` checks if `a` is of type `int`.
13. **Comparison with None**: You can use the `is` operator to check if a variable is `None`. For example, `if x is None:` checks if `x` is `None`.
14. **Comparison with Strings**: String comparisons are case-sensitive and lexicographical. For example, `'apple' < 'banana'` evaluates to `True` because `'a'` comes before `'b'` in the ASCII table.
15. **Comparison with Lists**: List comparisons are done element-wise. For example, `[1, 2] < [1, 3]` evaluates to `True` because `2` is less than `3`.
16. **Comparison with Dictionaries**: Dictionary comparisons are not directly supported, but you can compare their keys and values separately.
17. **Comparison with Tuples**: Tuple comparisons are done element-wise, similar to list comparisons. For example, `(1, 2) < (1, 3)` evaluates to `True` because `2` is less than `3`.
18. **Comparison with Sets**: Set comparisons are not directly supported, but you can compare their elements using membership operators.
19. **Comparison with Custom Objects**: You can define custom comparison methods in your classes to enable comparison between instances of your class.
20. **Comparison with Boolean Values**: In Python, `True` is considered greater than `False`. For example, `True > False` evaluates to `True`.
21. **Comparison with Floating-Point Numbers**: Floating-point comparisons may introduce small rounding errors due to the way numbers are represented in memory. To mitigate this, you can use the `math.isclose()` function to compare floating-point numbers with a specified tolerance.
# 22. **Comparison with Integers**: Integer comparisons are straightforward and do not introduce rounding errors.
# 23. **Comparison with Complex Numbers**: Complex numbers cannot be directly compared using comparison operators. You can compare their real and imaginary parts separately.

"""
a=10
b=20
c=10
# print(a==b)  # Output: False
# print(a!=b)  # Output: True
# print(a>b)   # Output: False
# print(a<b)   # Output: True
# print(a>=b)  # Output: False
# print(a<=b)  # Output: True
# print(a==c)  # Output: True
# print(a!=c)  # Output: False
# print(a is b)  # Output: False
# print(a is c)  # Output: True
#why true? -- Beause a and c are pointing to the same object in memory
# print(a is not b)  # Output: True 
# print(a is not c)  # Output: False
# print(a in [1,2,3,4,5])  # Output: False
# print(a not in [1,2,3,4,5])  # Output: True
# print(a in [10,20,30])  # Output: True
# print(a not in [10,20,30])  # Output: False
# print(a in [10,20,30] and b in [10,20,30])  # Output: True
# print(a in [10,20,30] or b in [10,20,30])  # Output: True
# print(a<b<c)
a=305
b=305
print(a is b)