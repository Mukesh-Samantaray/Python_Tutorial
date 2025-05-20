"""
Lets learn about while loops in Python.
A while loop in Python is used to execute a block of code repeatedly as long as a given condition is true. The syntax for a while loop is as follows:
while condition:
    # code to execute while the condition is true   
# Example:
count = 0
while count < 5:
    print(count)
    count += 1  
# Output:
# 0
# 1
# 2
# 3
# 4
# The while loop can also be used to create an infinite loop, which will run indefinitely until it is interrupted or a break statement is encountered.
# Example:
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count == 5:
#         break
# # Output:
# # 0
# # 1
# # 2
# # 3
# # 4
# The while loop can also be used with the continue statement to skip the current iteration and move to the next one.
# Example:
# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print(count)
# # Output:
# # 1
# # 2
# # 4
# # 5
# The while loop can also be used with the else statement, which will execute after the loop has completed normally (i.e., not interrupted by a break statement).
# Example:
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print("Loop completed")
# # Output:
# # 0
# # 1
# # 2
# # 3
# # 4
# # Loop completed
# The while loop can also be used with the pass statement, which does nothing and is used as a placeholder.
# Example:
# count = 0
# while count < 5:
#     pass
#     count += 1
# print("Count:", count)
# # Output:
# # Count: 5
# The while loop can also be used with the break statement to exit the loop prematurely.
# Example:
# count = 0
# while count < 5:
#     print(count)
#     count += 1
#     if count == 3:
#         break
# # Output:
# # 0
# # 1
# # 2

"""
