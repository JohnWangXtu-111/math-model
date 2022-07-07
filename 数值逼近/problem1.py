import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import interpolate
import pylab as pl

# 中文显示问题
plt.rcParams['font.sans-serif']=['Simhei']

# 负号显示问题
matplotlib.rcParams['axes.unicode_minus'] =False


# 数据样本点
x_data = np.linspace(0, 2.25 * np.pi, 10)
y_data = np.sin(x_data)


x_new = np.linspace(0, 2.25 * np.pi, 10000)

# 线性插值
f_linear = interpolate.interp1d(x_data, y_data)
y_linear = f_linear(x_new)

# 样条插值
tck = interpolate.splrep(x_data, y_data)
y_bspline =  interpolate.splev(x_new, tck)


# 可视化
plt.figure()
plt.xlabel(u"安培")
plt.ylabel(u"伏特")
plt.plot(x_data, y_data, "o",label="原始数据", color="red")
plt.plot(x_new, y_linear, label="线性插值")
plt.plot(x_new, y_bspline, label="样条插值")


pl.legend()
pl.show()