from sympy import *

x = symbols('x')

print(limit(sin(x) / x, x, 0))

print(limit((1 + 1 / x) ** x, x, oo))