"""
 before going to loops, let's see the range function
        
        range(start, stop, step)

range(10) # this will give us a range object from 0 to 9
# range(1, 10) # this will give us a range object from 1 to 9
# range(1, 10, 2) # this will give us a range object from 1 to 9 with a step of 2
# range(10, 1, -1) # this will give us a range object from 10 to 2 with a step of -1
# range(10, 1, -2) # this will give us a range object from 10 to 2 with a step of -2
"""
# num=range(1,10,2)
# print(num)
# print("odd numbers between 1 and 10:",list(num))
# print("even numbers between 1 and 10:",list(range(2,10,2)))
"""
for loop
The for loop in Python is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. The syntax is as follows:
for variable in iterable:
    # code to execute for each item in the iterable
Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)    
# Output:
# apple
# banana
# cherry
# The for loop can also be used with the range() function to iterate over a sequence of numbers.
# Example:
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# The for loop can also be used with the enumerate() function to get the index and value of each item in a list.
# Example:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry
# The for loop can also be used with the zip() function to iterate over two or more lists at the same time.
# Example:
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
for fruit, vegetable in zip(fruits, vegetables):
    print(fruit, vegetable)
# Output:
# apple carrot
# banana broccoli
# cherry spinach

"""
''''
Print sum of all odd numbers between 0 and 10
sum=0
for i in range(10):
    print(i)
    if i%2!=0:
        sum+=i
print("Sum of all odd numbers between 0 and 10:",sum)

'''

# check if a number is prime or not
# num=int(input("Enter a number: "))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")


'''
num=0
fact=1
if num==0:
    print(1)
elif num>0:
    if num==1:
        print(1)
    else: 
        for i in range(1,num+1):
            fact*=i
        print("Factorial of",num,"is",fact)
        '''
# digit=[1,2,4]
# (str(d) for d in digit)
# print(str(digit))
