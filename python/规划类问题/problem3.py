# 线性规划 --> 运输问题
import pulp
import numpy as np

## 分别对应列和行上的求和
def transport(c, a, b):
    colLen = len(b)
    rowLen = len(a)
    # 定义线性规划问题
    prob = pulp.LpProblem("tranport problem", sense=pulp.LpMaximize)
    # 决策变量x
    x = [[pulp.LpVariable(f'x{i}{j}', lowBound=0)
          for j in range(colLen)] for i in range(rowLen)]

    def flatten(x): return [y for l in x for y in flatten(
        l)] if type(x) is list else [x]

    prob += pulp.lpDot(flatten(x), c.flatten())

    for i in range(rowLen):
        prob += (pulp.lpSum(x[i]) <= a[i])

    for j in range(colLen):
        prob += (pulp.lpSum([x[i][j] for i in range(rowLen)]) <= b[j])

    prob.solve()
    print(pulp.value(prob.objective))


# test
costs = np.array([[500, 550, 630, 1000, 800, 700],
                  [800, 700, 600, 950, 900, 930],
                  [1000, 960, 840, 650, 600, 700],
                  [1200, 1040, 980, 860, 880, 780]])
max_plant = [76, 88, 96, 40]
max_cultivation = [42, 56, 44, 39, 60, 59]
transport(costs, max_plant, max_cultivation)
