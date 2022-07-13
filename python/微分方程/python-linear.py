import sympy as sp
A=sp.Matrix([[2, 1, -5, 1],[1, -3, 0, -6],[0, 2, -1, 2],[1, 4, -7, 6]])
b=sp.Matrix([8, 6, -2, 2]); b.transpose()
print("系数矩阵A的秩为:",A.rank())
# A --> 对矩阵求逆矩阵
# x = A^-1 *  b
print("线性方程组的唯一解为:",A.inv()*b)