# 线性规划
import pulp
import numpy as np

# 目标函数系数
z = np.array([2, 3, 1])

# 不等式约束
A = np.array([[1, 4, 2], [1, 2, 0]])
b = np.array([8, 6])

# 等式约束
Aeq = [[1, 2, 4]]
beq = [101]
# 确定问题 max or min
m = pulp.LpProblem(sense=pulp.LpMaximize)

# 定义三个变量放到列表中
x = [pulp.LpVariable(f'x{i}', lowBound=0) for i in [1, 2, 3]]  # [x1, x2, x3]

# 定义目标函数 z[i] * x[i] --> 求和
m += pulp.lpDot(x, z)  # 按位相乘再相加

# 不等于约束
for i in range(len(A)):
    m += (pulp.lpDot(A[i], x) >= b[i])

# 等式约束、
for i in range(len(Aeq)):
    m += (pulp.lpDot(Aeq[i], x) == beq[i])


# 求解
m.solve()
# 输出结果
# 优化结果
print(pulp.value(m.objective))
# 决策变量
print([pulp.value(var) for var in x])
