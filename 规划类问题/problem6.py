from scipy.optimize import minimize
import numpy as np

# 定义待求解的函数
def fun(args):
    a,b,c,d = args
    v = lambda x: (a + x[0]) / (b + x[1]) - c * x[0] + d * x[2]
    return v


# 约束条件
def con(args):
    x1min,x1max,x2min,x2max,x3min,x3max = args
    cons = ({'type':'ineq','fun':lambda x : x[0] - x1min},\
        {'type':'ineq','fun':lambda x:-x[0] + x1max},\
        {'type':'ineq','fun':lambda x:x[1] - x2min},\
        {'type':'ineq','fun':lambda x:-x[1] + x2max},\
        {'type':'ineq','fun':lambda x:x[2] - x3min},\
        {'type':'ineq','fun':lambda x:-x[2] + x3max})
    return cons

args = (2,1,3,4)
args1 = (0.1, 0.9,0.1, 0.9,0.1, 0.9)
cons = con(args1)

x0 = np.asarray((0.5,0.5,0.5))
res = minimize(fun(args), x0, method='SLSQP',constraints=cons)
print(res)