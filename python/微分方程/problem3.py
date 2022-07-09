from sympy import *
k = symbols('k')

print(summation(1 / (k ** 2), (k, 1, oo)))