import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


ax = plt.axes(projection='3d')

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
x_new = np.linspace(-1, 1, 50)
y_new = np.linspace(-1, 1, 50)

f = interpolate.interp2d(x_data, y_data, z_data, kind="cubic")
# 不需要网格化
z_new = f(x_new, y_new)

# ax.plot_surface(x_data, y_data, z_data, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
# ax.set_title('原始数据')

ax.plot_surface(x_new, y_new, z_new, rstride=5, cstride=5, cmap='viridis', edgecolor='none')
ax.set_title('样条插值')

plt.show()