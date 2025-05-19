"""
Assignment Operators
Assignment operators are used to assign values to variables.
They are used to assign values to variables in Python.
The assignment operator is represented by the equal sign `=`.
The assignment operator assigns the value on the right side to the variable on the left side.
Assignment operators can also be combined with arithmetic operators to perform operations and assign the result to a variable in a single step. 
For example, `+=` adds a value to a variable and assigns the result back to that variable.
The following are the most common assignment operators in Python:
1. **Assignment (`=`)**: Assigns the value on the right to the variable on the left.
2. **Addition Assignment (`+=`)**: Adds the value on the right to the variable on the left and assigns the result back to the variable.
3. **Subtraction Assignment (`-=`)**: Subtracts the value on the right from the variable on the left and assigns the result back to the variable.
4. **Multiplication Assignment (`*=`)**: Multiplies the variable on the left by the value on the right and assigns the result back to the variable.
5. **Division Assignment (`/=`)**: Divides the variable on the left by the value on the right and assigns the result back to the variable.
6. **Floor Division Assignment (`//=`)**: Performs floor division on the variable on the left by the value on the right and assigns the result back to the variable.
7. **Modulus Assignment (`%=`)**: Performs modulus operation on the variable on the left by the value on the right and assigns the result back to the variable.
8. **Exponentiation Assignment (`**=`)**: Raises the variable on the left to the power of the value on the right and assigns the result back to the variable.
9. **Bitwise AND Assignment (`&=`)**: Performs a bitwise AND operation on the variable on the left with the value on the right and assigns the result back to the variable.
10. **Bitwise OR Assignment (`|=`)**: Performs a bitwise OR operation on the variable on the left with the value on the right and assigns the result back to the variable.
11. **Bitwise XOR Assignment (`^=`)**: Performs a bitwise XOR operation on the variable on the left with the value on the right and assigns the result back to the variable.
12. **Bitwise Left Shift Assignment (`<<=`)**: Performs a left shift operation on the variable on the left by the value on the right and assigns the result back to the variable.
13. **Bitwise Right Shift Assignment (`>>=`)**: Performs a right shift operation on the variable on the left by the value on the right and assigns the result back to the variable.
14. **Chained Assignment**: You can assign the same value to multiple variables in a single line using chained assignment. For example, `x = y = z = 10` assigns the value `10` to all three variables `x`, `y`, and `z`.
15. **Multiple Assignment**: You can assign multiple values to multiple variables in a single line using tuple unpacking. For example, `x, y, z = 1, 2, 3` assigns `1` to `x`, `2` to `y`, and `3` to `z`.
16. **Augmented Assignment with Lists**: You can use augmented assignment operators with lists to modify their contents. For example, `my_list += [4, 5]` appends `[4, 5]` to `my_list`.    
#
# """   
#
# # a = 10
# # b = 20
# # a += b
# # print("a += b:", a)  # Output: 30
# # a -= b
# # print("a -= b:", a)  # Output: 10
# # a *= b
# # print("a *= b:", a)  # Output: 200
# # a /= b
# # print("a /= b:", a)  # Output: 10.0
# # a //= b
# # print("a //= b:", a)  # Output: 0.5
# # a %= b
# # print("a %= b:", a)  # Output: 0.5
# # a **= b
# # print("a **= b:", a)  # Output: 0.5
# # a &= b
# # print("a &= b:", a)  # Output: 0.5
# # a |= b
# # print("a |= b:", a)  # Output: 0.5
# # a ^= b
# # print("a ^= b:", a)  # Output: 0.5
a=b=[1,2,3]
print(a)
print(b)
a+=[4,5,6]
print(a)
print(b)
a=a+[7,8,9]
print(a)
print(b)

x=y=z=20
x+=y
print(x,y,z)
y=y+20
print(x,y,z)    
