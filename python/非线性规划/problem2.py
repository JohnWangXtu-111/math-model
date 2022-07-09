from scipy.optimize import minimize
import numpy as np


def func(x):
    x1, x2, x3, x4, x5 = x
    return x1 ** 2 + x2 ** 2 + 3 * x3 ** 2 + 4 * x4 ** 2 + 2 * x5 ** 2 - 8 * x1 - 2 * x2 - 3 * x3 - x4 - 2 * x5


A = np.array([[1, 1, 1, 1, 1], [1, 2, 2, 1, 6],
              [2, 1, 6, 0, 0], [0, 0, 1, 1, 5]])


b = np.array([400, 800, 200, 200])

# np.dot()向量点乘或矩阵乘法
cons = {'type': 'ineq', 'fun': lambda x: b-A@x}
bd = [(0, 99) for i in range(A.shape[1])]

res = minimize(func, np.ones(5), constraints=cons, bounds=bd)
print(res.fun)
print(res.success)
print(res.x)
