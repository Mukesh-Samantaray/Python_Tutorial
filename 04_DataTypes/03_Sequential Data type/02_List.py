import statistics

"""
list
# A list is a collection of items that are ordered and changeable.
# Lists are written with square brackets [].
# Lists can contain items of different data types, including other lists.
# Lists are mutable, meaning you can change, add, or remove items after the list has been created.
# Lists are indexed, meaning you can access items in the list using their index (position) in the list.
# The index of the first item in a list is 0, the second item is 1, and so on.
# The index of the last item in a list is -1, the second-to-last item is -2, and so on.
# Lists can be nested, meaning you can have a list inside another list.
# Lists can be sliced, meaning you can access a range of items in the list using their index.
# Lists can be concatenated, meaning you can combine two or more lists into one list using the + operator.
# Lists can be repeated, meaning you can repeat a list multiple times using the * operator.
# Lists can be sorted, meaning you can arrange the items in the list in a specific order using the sort() method.
# Lists can be reversed, meaning you can reverse the order of the items in the list using the reverse() method.
# Lists can be copied, meaning you can create a copy of the list using the copy() method.
# Lists can be cleared, meaning you can remove all items from the list using the clear() method.
# Lists can be counted, meaning you can count the number of occurrences of a specific item in the list using the count() method.
# Lists can be extended, meaning you can add multiple items to the end of the list using the extend() method.
# Lists can be inserted, meaning you can add an item at a specific index in the list using the insert() method.
# Lists can be removed, meaning you can remove a specific item from the list using the remove() method.
# Lists can be popped, meaning you can remove an item from the list at a specific index using the pop() method.
# Lists can be joined, meaning you can join the items in the list into a single string using the join() method.
# Lists can be split, meaning you can split a string into a list of items using the split() method.
# Lists can be enumerated, meaning you can get the index and value of each item in the list using the enumerate() function.
# Lists can be zipped, meaning you can combine two or more lists into a list of tuples using the zip() function.
# Lists can be unpacked, meaning you can assign the items in a list to multiple variables using the unpacking operator (*).
# Lists can be iterated, meaning you can loop through the items in the list using a for loop.
# Lists can be filtered, meaning you can create a new list with items that meet a specific condition using a list comprehension.
# Lists can be mapped, meaning you can apply a function to each item in the list using the map() function.
# Lists can be reduced, meaning you can apply a function to reduce the list to a single value using the reduce() function.
# Lists can be flattened, meaning you can convert a nested list into a single list using a list comprehension or the itertools.chain() function.
# Lists can be sorted in reverse order using the sort() method with the reverse parameter set to True.


"""
# #Example on each of the above
# # 1. Create a list
# my_list = [1, 2, 3, 4, 5]
# print("Original list:", my_list)
# # 2. Access items in a list
# print("First item:", my_list[0])
# print("Last item:", my_list[-1])
# # 3. Change items in a list
# my_list[0] = 10
# print("Changed first item:", my_list)
# # 4. Add items to a list
# my_list.append(6)
# print("Added item:", my_list)
# # 5. Remove items from a list
# my_list.remove(10)
# print("Removed item:", my_list)
# # 6. Insert items in a list
# my_list.insert(0, 67)
# print("Inserted item:", my_list)
# # 7. Sort a list
# my_list.sort()
# print("Sorted list:", my_list)
# # 8. Reverse a list
# my_list.reverse()
# print("Reversed list:", my_list)
# # 9. Copy a list
# my_list_copy = my_list.copy()
# print("Copied list:", my_list_copy)
# # 10. Clear a list
# my_list.clear()
# print("Cleared list:", my_list)
# # 11. Count items in a list
# my_list_copy.append(1)
# my_list_copy.append(2) 
# my_list_copy.append(1)
# print("Count of 1:", my_list_copy.count(1))
# # 12. Extend a list
# my_list_copy.extend([3, 4, 5])
# print("Extended list:", my_list_copy)
# #pop from list
# # 13. Pop an item from a list
# popped_item = my_list_copy.pop()
# print("Popped item:", popped_item)
'''
list comprehension
# List comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The expression is evaluated for each item in the iterable, and the result is added to the list.
# List comprehension can be used to create a new list by applying an expression to each item in an existing list.
# It can also be used to filter items in a list by applying a condition.
# List comprehension is often more readable and faster than using a for loop to create a list.
# List comprehension can be used to create a list of squares of numbers from 1 to 10.
# Example:
squares = [x**2 for x in range(1, 11)]
# print(squares)
# # Output:
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # List comprehension can also be used to create a list of even numbers from 1 to 10.
# Example:
evens = [x for x in range(1, 11) if x % 2 == 0]
# print(evens)
# # Output:
# # [2, 4, 6, 8, 10]
# # List comprehension can also be used to create a list of tuples.
# Example:
tuples = [(x, x**2) for x in range(1, 6)]
# print(tuples)
# # Output:
# # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# # List comprehension can also be used to create a list of strings.
# Example:
strings = [str(x) for x in range(1, 6)]
# print(strings)
# # Output:
# # ['1', '2', '3', '4', '5']
# # List comprehension can also be used to create a list of lists.
# Example:
lists = [[x, x**2] for x in range(1, 6)]
# print(lists)
# # Output:
# # [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]
# # List comprehension can also be used to create a list of dictionaries.
# Example:
dictionaries = [{x: x**2} for x in range(1, 6)]
# print(dictionaries)
# # Output:
# # [{1: 1}, {2: 4}, {3: 9}, {4: 16}, {5: 25}]
# # List comprehension can also be used to create a list of sets.
# Example:

# # Output:

'''
'''All Delete , remove ,clear,pop ration on list '''

# Num=[2,4,6,7]
# Num.remove(6)--- .remove() can remove specific value from the list
# print(Num)

# Num=[2,4,5]
# del Num[0:2]# --- Del is used before the name of the list and can delete range of index list
# print(Num)

# num=[2,3,4,5,6]
# del num#------------ del is a statement even it can delete the list, means no memorylocation found
# print(num)

# num=[1,2,3,4]
# num.pop()  #--- .pop() method is used to delete the last element of list
# print(num)

# num=[1,2,3]
# num.pop(0) #---- .pop() method takes index as parameter
# print(num)

# num=[6,7,8,9]
# num.clear()#--- remember .clear() does not take any arguments it clears the list and give empty list as output
# print(num)

''' add,insert, extend,change with index,append() '''
# Num_list=[1,2,3,4]
# Num_list.insert(3,0)#--- .insert() method takes 2 argument , one is position 2nd one is the value you want to insert , you can not give single argument
# print(Num_list)


# num=[0,1,2,3,4]
# print(num[0])
# num[0]=1 # ---- alternatively you can directly assign any value to that using index value
# print(num)

# num=[0,12,3,4,5]
# num.append("\"a\"") # --- .append() takes value that to be inserted to the list as argument  and you can append any type of data 
# print(num)

# num=[2,3,4,5]
# b="c"
# num.extend(b)# --- .extend() appends the iterable objects only , you can not give int or float value 
# print(num)

# num=[]
# num.extend("Magic") # Convert any string to list of characters
# print(num)


""" Some Built in Function used to find max, min, avg ,length, count,sort ,reverse"""

# num=[-1,1,2,3,3,5,7,6]
# print(num,id(num))
# print(max(num))
# print(min(num))
# print(len(num))



# print(num.count(3))



# num.sort()# returns none it modifies the same list in sorted order ,
# print(num,id(num))


# print(sorted(num),id(sorted(num))) # it sort the list and assign into another list and  returns

# mlist=[1,2,3,5,3,7,8]
# x=enumerate(mlist)#-- enumerate (iterable,start index(by deafult index=0)): it adds counter to the index, it returns enumerate object contain index and value of a list
# print(tuple(x),type(x))#-- its a special type of iterator 

"""  list objects are iterable """
# l=[1,2,3,4]
# # for i in l:
# #     print(i)#-- Print all the elements in a list

# for i in range(len(l)):
#     print("index:",i,"value:",l[i])#--- print index and range

# for i,v in enumerate(mlist):
#     print((i,v))

""" List slicing""" # v.v.v important concept when negative slicing comes into picture
# mlist=[1,2,3,4,5]
# print(mlist[::-1])

""" Rotate a list  """
mlist=[1,2,3,4,5]
for i in range(len(mlist)-1,0,-1):
    mlist[i]=mlist[i-1]
    print(mlist)


