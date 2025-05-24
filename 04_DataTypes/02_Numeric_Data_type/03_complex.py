"""  
Complex numbers in Python
Complex numbers are numbers that have both a real part and an imaginary part.
In Python, complex numbers are represented using the complex class. The imaginary part is represented using the letter 'j' or 'J'.
Complex numbers can be created using the complex() function or by using the 'j' or 'J' suffix.

"""
# Example of complex numbers
a = 3 + 4j
b = 2 - 3j
c = complex(1, 2)  # real part = 1, imaginary part = 2
d = complex(3.5, 4.5)  # real part = 3.5, imaginary part = 4.5
e = complex(0, 1)  # pure imaginary number
f = complex(1, 0)  # pure real number
g = complex(0, 0)  # zero complex number
h = complex(1, -1)  # complex number with negative imaginary part
i = complex(-1, 1)  # complex number with negative real part    
j = complex(-1, -1)  # complex number with negative real and imaginary part
k = complex(1.5, -2.5)  # complex number with float real and imaginary part
l = complex(-1.5, 2.5)  # complex number with float negative real and imaginary part
m = complex(1.5, 0)  # complex number with float real part and zero imaginary part
n = complex(0, -2.5)  # complex number with zero real part and float negative imaginary part
o = complex(0, 0.5)  # complex number with zero real part and float positive imaginary part
p = complex(1.5, 2.5)  # complex number with float real and imaginary part
q = complex(-1.5, -2.5)  # complex number with float negative real and imaginary part
r = complex(1.5, -2.5)  # complex number with float real part and negative imaginary part
s = complex(-1.5, 2.5)  # complex number with float negative real part and imaginary part
t = complex(1.5, 0)  # complex number with float real part and zero imaginary part
print("a:", a, type(a))
print("b:", b, type(b))
print("c:", c, type(c))
print("d:", d, type(d))
print("e:", e, type(e))
print("f:", f, type(f))
print("g:", g, type(g))
print("h:", h, type(h))
print("i:", i, type(i))
