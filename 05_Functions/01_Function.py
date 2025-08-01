'''
1.what is function?
-- function is reusable block of codes to perform specific task
--code reusability
--breakdown complex program into smaller chunks
--provides error free programming

2.How a function is defined or what is function defination
-- a function is defined using def keyword followed by function name followed by parameters within open brackets followed by colon.
eg:- def sum(num1,num2):
        return num1+num2
     result= sum(1,2) 
     print(result)  

'''
'''   
def sum(num1,num2):
         print(num1+num2)
result= sum(1,2) 
print(result)

 -- 3
 None
'''

'''
3.The pass statement serves as a placeholder for future code, preventing errors from empty code blocks.

def future_function():
    pass-----u can not leave this empty cause it is code area of function it will throw error

# this will execute without any action or error
future_function()  

It's typically used where code is planned but has yet to be written.
'''
'''
1. def future_function(a,b):
    # error no code is there
  future_function(d,f)  


 2. def future_function(a,b):
      c=a+b
      return c
print(future_function(5,6) ) 
  
# # will produce output none as return is not there
# # if you listed parameters inside paranthesis you have to provide arguments
# print(future_function(5,6) ) 
'''

""" Functions are of two types

--pre-defined and user defined 

 pre defined--print(),len(),type(),list(),int(),float()

"""
'''
Very Very Important
-----------------------------------
def Name():
    print("Mukesh")
print(Name()) 
----------------------------------------
output-Mukesh
       None
'''
'''
-------------------------------------------------------------------------------------
# if we store  any function in a variable then it will always hold the return value.
def Name(num1,num2):
     c=num1+num2
h=Name(2,3) 
print(h)
-----------------------------------------------------------------------------------
''' 
'''
types of functional arguments
-- 4 types
1.positional-- return in same order we give input--
     def Name(First,Last):
    return First+" "+Last
Nm=Name('Mukesh', 'Samantaray')
print(Nm) 
-------------- number of arguments should be same

2. Keyword Arguments

A keyword argument is an argument passed to a function by explicitly specifying the parameter name, regardless of its position.

---order is not important
  i.def Name(F,L)
     return F+" "+L
   print(Name(L="s",F="M"))

  ii.def Name(First,Last):
      return First+" "+Last
    Nm=Name('Mukesh', First='Samantaray')
    print(Nm)  
--TypeError: Name() got multiple values for argument 'First' 
  
--keyword arguments follows positional argument
iii.def Name(F,L)
     return F+" "+L
print(Name(L="s","M"))

SyntaxError: positional argument follows keyword argument

----------

3.Default argument

 default argument in Python is a parameter that takes a default value if no argument is provided when the function is called.
 
   --- order is important
  --- no of argument may or may not be equal
  i.def greetings(name='python'):
     print("Hy"+" "+name)
    greetings() --no arguments
  ----  Hy python
  ii.def greetings(name='python'):
      print("Hy"+" "+name)
     greetings('Ramesh')  --with arguments

4.Variable length Argument

i.  *args

--- takes only positional arguments
-----data type is tuple

   e.g :
         def printx(*args):
           print(args)
           print(type(args))
         printx()

   e.g: def printx(*args):
           print(args)
           print(type(args))
        printx('harsh',"rajesh")

ii.**args

    

'''
'''

'''
def printx(*args,**kargs):
    '''ok'''
    for i in args:
          print(sum(i))
    
    for i, j in kargs.items():
           
           print(f'Key:{i},Value :{j}')
           print(type(kargs))
    list = []       
    for i in kargs.keys():
        list.append(i)
        print(list)       
printx((1,2,3,4),ds="harsh",js="rajesh") #-----------------Create Dictionary

