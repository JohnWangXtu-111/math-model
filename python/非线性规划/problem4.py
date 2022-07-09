from scipy.optimize import minimize
import numpy as np


def fun(x):
    x1, x2 = x
    return 2 * x1**2 - 4 * x1*x2 + 4 * x2**2 - 6*x1 - 3*x2


cons = ({'type': 'ineq', 'fun': lambda x: 3 - x[0] - x[1]},
        {'type': 'ineq', 'fun': lambda x: 9 - 4 * x[0] - x[1]})
res = minimize(fun, np.ones(2), constraints=cons,
               bounds=((0, None), (0, None)))

print(res.fun)
print(res.x)
