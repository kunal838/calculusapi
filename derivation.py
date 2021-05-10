from sympy import *

x = Symbol('x')
def derviation(n): 
   
    y = Symbol('y')
   
    z = diff(n , x)
    return print("value of z is :" + str(z))


derviation(sin(x))