import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

# 定义拟合函数形式


def func(p, x):
    a, k = p
    return a * x + k

# 定义loss的计算方法


def error(p, x, y):
    return func(p, x) - y


x = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
y = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])


# 给定参数初始值
p0 = (2, 2)
# 进行拟合
para = leastsq(error, p0, args=(x, y))
# 画出拟合后的曲线
# y_fitted = func(para[0], x)
x_new = np.linspace(0, 10, 1000)
k, b = para[0]
y_new = x_new * k + b

plt.figure()
plt.scatter(x, y,label="原始离散数据")
plt.plot(y_new, x_new, label="拟合曲线")

plt.show()