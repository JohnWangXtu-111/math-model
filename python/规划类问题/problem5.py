# 非线性规划
from scipy.optimize import minimize
import numpy as np

def fun(args):
    a = args
    v = lambda x:a/x[0] + x[0]
    return v

args = 1

x0 = np.asarray(2)
res = minimize(fun(args), x0, method='SLSQP')

print(res)