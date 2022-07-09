# 线性规划
from scipy.optimize import linprog
import numpy as np


# 参数信息
c = np.array([2, 3, -5])

A = np.array([[-2, 5, -1], [1, 3, 1]])
b = np.array([-10, 12])

Aeq = np.array([[1, 1, 1]])
beq = np.array([7])


res = linprog(c, A, b, Aeq, beq, bounds=((0, None), (0, None), (0, None)))

print("目标函数最优", res.fun)
print("最优解", res.x)
