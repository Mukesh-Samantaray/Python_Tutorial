"""
Bitwise Operators
Bitwise operators are used to perform bit-level operations on integers.
They operate on the binary representation of integers and return an integer as a result.
The following are the most common bitwise operators in Python:
1. **Bitwise AND (`&`)**: Performs a bitwise AND operation on two integers. The result has a `1` in each bit position where both operands have a `1`.
2. **Bitwise OR (`|`)**: Performs a bitwise OR operation on two integers. The result has a `1` in each bit position where at least one operand has a `1`.
3. **Bitwise XOR (`^`)**: Performs a bitwise XOR operation on two integers. The result has a `1` in each bit position where the operands differ (one is `1` and the other is `0`).
4. **Bitwise NOT (`~`)**: Performs a bitwise NOT operation on an integer. The result inverts all the bits of the operand (changes `1` to `0` and `0` to `1`).
5. **Bitwise Left Shift (`<<`)**: Shifts the bits of an integer to the left by a specified number of positions. This is equivalent to multiplying the integer by `2` raised to the power of the number of positions shifted.
6. **Bitwise Right Shift (`>>`)**: Shifts the bits of an integer to the right by a specified number of positions. This is equivalent to dividing the integer by `2` raised to the power of the number of positions shifted.
7. **Bitwise Assignment Operators**: Bitwise operators can also be combined with assignment operators to perform bitwise operations and assign the result back to the variable in a single step. For example, `&=` performs a bitwise AND operation and assigns the result back to the variable.    
8. **Operator Precedence**: Bitwise operators have a specific order of precedence when evaluating expressions. For example, bitwise AND has higher precedence than bitwise OR.
9. **Bitwise Operations on Negative Numbers**: Bitwise operations on negative numbers are performed using two's complement representation. The result may not be intuitive, so it's important to understand how negative numbers are represented in binary.
10. **Bitwise Operations on Floats**: Bitwise operators cannot be directly applied to floating-point numbers. You need to convert them to integers first.
11. **Bitwise Operations on Strings**: Bitwise operators cannot be directly applied to strings. You need to convert them to integers first.
12. **Bitwise Operations on Lists**: Bitwise operators cannot be directly applied to lists. You need to convert them to integers first.
13. **Bitwise Operations on Tuples**: Bitwise operators cannot be directly applied to tuples. You need to convert them to integers first.
14. **Bitwise Operations on Sets**: Bitwise operators cannot be directly applied to sets. You need to convert them to integers first.
15. **Bitwise Operations on Dictionaries**: Bitwise operators cannot be directly applied to dictionaries. You need to convert them to integers first.
16. **Bitwise Operations on Custom Objects**: You can define custom bitwise methods in your classes to enable bitwise operations between instances of your class.
17. **Bitwise Operations on Boolean Values**: Bitwise operators can be applied to boolean values, where `True` is treated as `1` and `False` is treated as `0`.


"""
# #Example on Each Bitwise Operator
# a = 10  # Binary: 1010
# b = 4   # Binary: 0100      
# # Bitwise AND
# bitwise_and = a & b  # Binary: 0000 (Decimal: 0)
# print("Bitwise AND:", bitwise_and)  # Output: 0
# # Bitwise OR
# bitwise_or = a | b  # Binary: 1110 (Decimal: 14)
# print("Bitwise OR:", bitwise_or)  # Output: 14
# # Bitwise XOR   
# bitwise_xor = a ^ b  # Binary: 1110 (Decimal: 14)
# print("Bitwise XOR:", bitwise_xor)  # Output: 14
# # Bitwise NOT
# bitwise_not = ~a  # Binary: 0101 (Decimal: -11)--- important to note that the result is negative because of two's complement representation
# # The bitwise NOT operator inverts all bits, including the sign bit.
# # In Python, integers are represented using two's complement, so the result is negative.
# print("Bitwise NOT:", bitwise_not)  # Output: -11

a=10
if a&1==0:
    print("Even")
else:
    print("Odd")
