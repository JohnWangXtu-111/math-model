import cvxpy as cp
import numpy as np

c = np.array([-1, -1])
A = np.array([[14, 9],[-6, 3]])
b = np.array([51, 1])

x = cp.Variable(2, integer=True)

obj = cp.Minimize(c * x)  # 构造目标函数
cons = [A * x <= b, x >= 0]  # 构造约束条件
prob = cp.Problem(obj, cons)  # 构建问题模型
prob.solve(solver='GLPK_MI', verbose=True)  # 求解问题
print("最优值为:", prob.value)
print("最优解为：\n", x.value)