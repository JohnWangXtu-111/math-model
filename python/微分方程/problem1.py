from sympy import *

t, gamma, omega0 = symbols('x gamma omega0')
x = Function('x')

eq = x(t).diff(t, 2) + 2 * gamma * omega0 * x(t).diff(t, 1) + omega0 ** 2  * x(t)


ans = dsolve(eq, x(t))
pprint(ans)