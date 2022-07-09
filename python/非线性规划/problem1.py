from scipy.optimize import minimize
from numpy import ones


def fun(x):
    x1, x2, x3 = x
    return (2 + x1) / (1 + x2) - 3 * x1 + 4 * x3


LB = [0.1]*3
UB = [0.9]*3
bound = tuple(zip(LB, UB))
res = minimize(fun, [1, 1, 1], bounds=bound)
print(res.fun, '\n', res.success, '\n', res.x)  # 输出最优值、求解状态、最优解
