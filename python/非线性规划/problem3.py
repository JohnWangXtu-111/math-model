from scipy.optimize import minimize
import numpy as np


def func(x):
    x1, x2, x3 = x
    return x1 ** 2 + x2 ** 2 + x3**2 + 8


cons = ({'type': 'ineq', 'fun': lambda x: x[0] ** - x[1] + x[2]**2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - x[1] ** 2 - x[2] ** 2 + 20},
        {'type': 'eq', 'fun': lambda x: -x[0] - x[1] ** 2 + 2},
        {'type': 'eq', 'fun': lambda x: x[0] + x[2] ** 2})

res = minimize(func, np.ones(3), constraints=cons,
               bounds=((0, None), (0, None), (0, None)))

print(res.fun)
print(res.x)