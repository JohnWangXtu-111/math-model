import numpy as np
from scipy.optimize import linear_sum_assignment


# 教师与课程一样多
# 各个教师对各个课的擅长程度矩阵
goodAt = np.array([[18, 5, 7, 16], [10, 16, 6, 5],
                  [11, 6, 4, 7], [13, 12, 9, 11]])
weakAt = 20-goodAt
row_ind, col_ind = linear_sum_assignment(weakAt)
print(row_ind)
for i in range(len(row_ind)):
    print("第" + str(row_ind[i]) + "老师" + "教" + "第" + str(col_ind[i]) + "门课")
