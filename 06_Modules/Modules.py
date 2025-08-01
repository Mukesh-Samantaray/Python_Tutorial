""" Modules in Python """
"""Module is a file that contains code to perform a specific task. A module may contain variables, functions, classes etc."""
"""As our programs grows bigger the lines of code will also increase.
   instead of putting all the codes in single file we can make different files to store them.
   it will make our code organized and easier to maintain """

import module1
print(module1.Mukesh)   

"""--- Each .py file in python is treated as module
   --- we can access any module from any package by importing it to the current module using import"""

import Mathematics.mathematics




"""We can access all the members of a module using modulename.(variable,function,class) """
print(Mathematics.mathematics.add(2,3))




"""We can also import specific member of module and use it directly"""
from Mathematics.mathematics import mul
print(mul(4,5))