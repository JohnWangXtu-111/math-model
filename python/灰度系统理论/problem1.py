# 关联性分析
import numpy as np


# 参考数列
X0 = np.array([18, 20, 22, 40, 44, 48, 60])

# 比较数列
X = np.array([
    [10, 15, 16, 24, 38, 40, 50],
    [3, 2, 12, 10, 22, 18, 20]
])

minus = []
for i in range(len(X)):
    minus.append(np.abs(X[i] - X0))

minus = np.array(minus)


row_len = minus.shape[0]
col_len = minus.shape[1]
# 最大差 最小差
min_tmp = []
max_tmp = []
for row_idx in range(row_len):
    min_tmp.append(np.min(minus[row_idx]))
    max_tmp.append(np.max(minus[row_idx]))

min = np.min(np.array(min_tmp))
max = np.max(np.array(max_tmp))

# 分辨系数
rho = 0.5

tmp = []

for i in range(row_len):
    t = []
    for k in range(col_len):
        t.append((min + rho * max) / (abs(X0[k] - X[i][k]) + rho * max))
    tmp.append(t)


ans = []

for i in range(row_len):
    ans.append(sum(tmp[i]))


ans = np.array(ans) / col_len
print(ans)
