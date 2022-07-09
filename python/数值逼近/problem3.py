import matplotlib
import numpy as np
from sympy import E
from scipy import interpolate
import pylab as pl


# 定义一下待插值的函数
def func(x, y):
    return (x + y) * np.exp(-5 * (x ** 2 + y ** 2))


# 原始数据
x_data = np.linspace(-1, 1, 15)
y_data = np.linspace(-1, 1, 15)

# 网格
x_data, y_data = np.meshgrid(x_data, y_data)
z_data = func(x_data, y_data)

# 样条插值
x_new = np.linspace(-1, 1, 100)
y_new = np.linspace(-1, 1, 100)

f = interpolate.interp2d(x_data, y_data, z_data, kind="cubic")
# 不需要网格化
z_new = f(x_new, y_new)
# 可视化

# subplot -> 表面图 extend 表示x y的数据范围，前面已经做成了网格
pl.subplot(121)
im1 = pl.imshow(z_data, extent=[-1, 1, -1, 1],
                cmap=matplotlib.cm.hot, interpolation='nearest', origin="lower")
pl.colorbar(im1)
pl.subplot(122)
im2 = pl.imshow(z_new, extent=[-1, 1, -1, 1], cmap=matplotlib.cm.hot,
                interpolation='nearest', origin="lower")
pl.colorbar(im2)
pl.show()
