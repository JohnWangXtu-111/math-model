import numpy as np
from scipy import interpolate
import matplotlib
import matplotlib.pyplot as plt
import pylab as pl

# 中文显示问题
plt.rcParams['font.sans-serif']=['Simhei']

# 负号显示问题
matplotlib.rcParams['axes.unicode_minus'] =False

# 原始数据
x_data = np.linspace(0, 10, 10)
y_data = np.sin(x_data)

# 0-5阶样条插值
arr = ['nearest', 'zero', 'linear', 'quadratic']

x_new = np.linspace(0, 10, 1000)
plt.figure()
for item in arr:
  f = interpolate.interp1d(x_data, y_data, kind=item)
  plt.plot(x_new, f(x_new), label=str(item))


plt.scatter(x_data, y_data, label="原始数据", color="green")
pl.legend()
pl.show()