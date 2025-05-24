"""
    Overview of Strings in Python:
    A string is an immutable sequence of Unicode characters. Strings are used to store text data and are defined using single, double, or triple quotes.

    String Creation:
    s1 = 'Hello'
    s2 = "World"
    

    String Indexing and Slicing:
    s = "Python"
    first = s[0]        # 'P'
    last = s[-1]        # 'n'
    slice1 = s[1:4]     # 'yth'
    slice2 = s[:2]      # 'Py'
    slice3 = s[2:]      # 'thon'
    reversed_s = s[::-1]# 'nohtyP'

    String Immutability:
    # Strings cannot be changed in place.
    # s[0] = 'J'  # Error

    String Concatenation and Repetition:
    s1 = "Hello"
    s2 = "World"
    concat = s1 + " " + s2   # 'Hello World'
    repeat = s1 * 3          # 'HelloHelloHello'

    String Membership:
    "ell" in s1      # True
    "x" not in s1    # True

    Common String Methods:
    s = " hello world "
    s.strip()        # 'hello world'
    s.lstrip()       # 'hello world '
    s.rstrip()       # ' hello world'
    s.upper()        # ' HELLO WORLD '
    s.lower()        # ' hello world '
    s.title()        # ' Hello World '
    s.capitalize()   # ' hello world '
    s.replace("l", "L") # ' heLLo worLd '
    s.count("l")     # 3
    s.find("world")  # 7
    s.index("world") # 7

    Splitting and Joining:
    words = s.split()             # ['hello', 'world']
    joined = "-".join(words)      # 'hello-world'

    String Formatting:
    name = "Alice"
    age = 30
    f"{name} is {age} years old." # 'Alice is 30 years old.'

    Checking String Content:
    "123".isdigit()     # True
    "abc".isalpha()     # True
    "abc123".isalnum()  # True
    s.startswith(" h")  # True
    s.endswith("d ")    # True

    Encoding and Decoding:
    encoded = s.encode("utf-8")
    decoded = encoded.decode("utf-8")

    Escape Characters:
    newline = "Line1\nLine2"
    # tab = "A\tB"

    Raw Strings:
    raw = r"C:\path\to\file"

    String Alignment:
    s.center(20)
    s.ljust(20)
    s.rjust(20)

    Iterating Over a String:
    for char in s:
        print(char)

    Comparing Strings:
    "a" == "A"      # False
    "a" < "b"       # True

    # Strings are powerful and flexible for text processing in Python.""" 





"""Here are some common Python string interview questions:

    1. What is a string in Python? How are strings stored in memory?
    2. Explain string immutability with an example.
    3. How do you reverse a string in Python?
    4. What is string slicing? Give examples.
    5. How do you check if a substring exists in a string?
    6. What is the difference between find() and index() methods?
    7. How do you convert a number to a string and vice versa?
    8. How do you split a string into a list? How do you join a list into a string?
    9. What are raw strings? When would you use them?
    10. How do you format strings in Python? Explain f-strings.
    11. What are some common string methods for case conversion?
    12. How do you remove whitespace from the beginning and end of a string?
    13. How do you count the occurrences of a character or substring in a string?
    14. How do you check if a string contains only digits, only alphabets, or is alphanumeric?
    15. How do you encode and decode strings in Python?
    16. How do you compare two strings in Python?
    17. What are escape characters? Give examples.
    18. How do you iterate over each character in a string?
    19. What is the output of s = "abc"; print(s*3)?
    20. How do you align strings (left, right, center) in Python?"""
    
"""
    # 1. What is a string in Python? How are strings stored in memory?
    # A string is an immutable sequence of Unicode characters. Strings are stored as objects in memory, and each character is a Unicode code point.

    # 2. Explain string immutability with an example.
    s = "hello"
    # s[0] = 'H'  # This will raise an error because strings are immutable.
    s = "Hello"  # You can create a new string instead.

    # 3. How do you reverse a string in Python?
    reversed_s = s[::-1]

    # 4. What is string slicing? Give examples.
    slice1 = s[1:4]  # Characters from index 1 to 3
    slice2 = s[:2]   # First two characters

    # 5. How do you check if a substring exists in a string?
    exists = "ell" in s  # True

    # 6. What is the difference between find() and index() methods?
    # find() returns -1 if substring not found; index() raises ValueError.
    s.find("e")    # 1
    # s.index("z") # Raises ValueError

    # 7. How do you convert a number to a string and vice versa?
    num = 123
    num_str = str(num)
    str_num = "456"
    num2 = int(str_num)

    # 8. How do you split a string into a list? How do you join a list into a string?
    words = "a b c".split()  # ['a', 'b', 'c']
    joined = "-".join(words) # 'a-b-c'

    # 9. What are raw strings? When would you use them?
    raw = r"C:\new\test"  # Backslashes are treated literally, useful for regex or file paths.

    # 10. How do you format strings in Python? Explain f-strings.
    name = "Alice"
    age = 30
    formatted = f"{name} is {age} years old."  # f-strings allow inline expressions.

    # 11. What are some common string methods for case conversion?
    upper = s.upper()
    lower = s.lower()
    title = s.title()
    capitalize = s.capitalize()

    # 12. How do you remove whitespace from the beginning and end of a string?
    trimmed = "  hello  ".strip()

    # 13. How do you count the occurrences of a character or substring in a string?
    count_l = s.count("l")  # 2

    # 14. How do you check if a string contains only digits, only alphabets, or is alphanumeric?
    "123".isdigit()     # True
    "abc".isalpha()     # True
    "abc123".isalnum()  # True

    # 15. How do you encode and decode strings in Python?
    encoded = s.encode("utf-8")
    decoded = encoded.decode("utf-8")

    # 16. How do you compare two strings in Python?
    "a" == "A"  # False (case-sensitive)
    "a" < "b"   # True (lexicographical order)

    # 17. What are escape characters? Give examples.
    newline = "Line1\nLine2"
    tab = "A\tB"

    # 18. How do you iterate over each character in a string?
    for char in s:
        pass  # Do something with char

    # 19. What is the output of s = "abc"; print(s*3)?
    # Output: abcabcabc

    # 20. How do you align strings (left, right, center) in Python?
    left = s.ljust(10)
    right = s.rjust(10)
    centered = s.center(10)
"""
