'''      Q)What is print() function in Python?
The print() function in Python is used to output data to the console or standard output device. 
It can take multiple arguments and can format the output in various ways. 
The print() function is versatile and can be customized using parameters like sep, end, file, and flush.

print() is used  to print specify message to the counsole
The print() function prints the given object to the standard output device (screen) or to the text stream file.

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Parameters:
objects: The objects to be printed. The objects are separated by a space by default.   
sep: The separator between the objects. By default, a space is used. 
end: The string appended after the last value, default a newline.
file: The file where the objects are printed. By default, it is sys.stdout (the console).
flush: A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False.

'''
# # Example:
# print("Hello, World!")
# print("Hello", "World", sep=" ", end="!\t")
# print("Hello", "World", sep="__", end="!\t")

"""
    Q)What Is Comment in Python?
    
A comment in Python is a line of text that is not executed as part of the program.
It is used to provide explanations or annotations for the code, making it easier to understand.
In Python, comments are created using the '#' symbol.
Single-line comments start with '#', and everything after it on that line is ignored by the interpreter.
we can use triple quoates for multi-line comments.

"""
# Example:
# print("Hello, World!")  # This prints "Hello, World!" to the console


'''


'''
"""
a=int("20",8)
print(a)

Why the output is 16?

# The output is 16 because the string "20" is interpreted as an octal (base 8) number.
In octal, the digits can only be 0-7.
The digit "2" in octal represents 2 in decimal, and the digit "0" represents 0 in decimal.
When you convert "20" from octal to decimal, it is calculated as:
2 * 8^1 + 0 * 8^0 = 16 + 0 = 16
# So, the decimal equivalent of the octal number "20" is 16.
"""