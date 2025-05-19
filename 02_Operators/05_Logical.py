"""
Logical Operators
Logical operators are used to combine conditional statements.
They return a Boolean value (`True` or `False`) based on the result of the logical operation.
The following are the most common logical operators in Python:
1. **Logical AND (`and`)**: Returns `True` if both operands are `True`, otherwise returns `False`.
2. **Logical OR (`or`)**: Returns `True` if at least one operand is `True`, otherwise returns `False`.
3. **Logical NOT (`not`)**: Returns `True` if the operand is `False`, otherwise returns `False`.
4. **Short-Circuit Evaluation**: In logical expressions, Python uses short-circuit evaluation, meaning it stops evaluating as soon as the result is determined. For example, in `a and b`, if `a` is `False`, `b` is not evaluated.
5. **Truthiness and Falsiness**: In Python, certain values are considered "truthy" (evaluating to `True`) or "falsy" (evaluating to `False`). For example, non-empty strings, non-zero numbers, and non-empty collections are truthy, while empty strings, zero, and empty collections are falsy.
6. **Boolean Context**: Logical operators can be used in conditional statements (e.g., `if`, `while`) to control the flow of the program based on the result of the logical operation.
7. **Bitwise Logical Operators**: Python also provides bitwise logical operators (`&`, `|`, `^`) that operate on the binary representation of integers. These operators perform bitwise AND, OR, and XOR operations, respectively.
8. **Operator Precedence**: Logical operators have a specific order of precedence when evaluating expressions. For example, `not` has higher precedence than `and`, which has higher precedence than `or`.
9. **Chained Logical Expressions**: You can chain multiple logical expressions together using parentheses to control the order of evaluation. For example, `(a and b) or (c and d)` evaluates `a and b` first, then combines the result with `c and d`.
10. **Comparison with Boolean Values**: In Python, `True` is considered greater than `False`. For example, `True > False` evaluates to `True`.


"""
a=1
b=30
c=90
print(a>b and a<c) # FALSE
print(a>b or a<c) # TRUE
print(not a)# TRUE
#example of logical operator precedence
print(a>b and a<c or b<c) # TRUE
#not>and>or