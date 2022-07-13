# GM(1, 1)
import numpy as np
import math
import matplotlib.pyplot as plt


X0 = np.array([18, 20, 22, 40, 44, 48, 60])
years = np.linspace(1977, 1983, 7, dtype=np.int16)
# 最开始应该检验数列的级比，这里忽略
length = X0.shape[0]

X1 = []

for i in range(length):
    if(i == 0):
        X1.append(X0[i])
    else:
        X1.append(X0[i - 1] + X0[i])

Z = []
rho = 0.5
for i in range(length):
    if(i == 0):
        Z.append(0)
    else:
        Z.append(rho * X1[i] + (1 - rho) * X1[i - 1])

Y = np.array(X0[1:])
Y = Y.reshape(length - 1, 1)
print(Y.shape)

Z = np.array(Z)
B = []

for i in range(Z.shape[0]):
    if(i != 0):
        B.append([-Z[i], 1])


B = np.array(B)

# a b参数
t1 = np.matmul(B.T, B)
# 矩阵求逆矩阵
t1 = np.linalg.inv(t1)

t1 = np.matmul(t1, B.T)
ans = np.matmul(t1, Y)


a = ans[0]
b = ans[1]

# 预测
Xhat1 = []

years1 = np.linspace(1977, 1983, 7)
for i in range(7):
    Xhat1.append((X0[1] - b / a) * pow(math.e, -a * (i - 1)) + b / a)


Xhat0 = []
Xhat0.append(0)

# 需要对预测值Xhat0检验 --> 残差...
for i in range(7):
    if(i != 0):
        Xhat0.append(Xhat1[i] - Xhat1[i - 1])

plt.figure()

plt.plot(years, X0)
plt.plot(years1, Xhat0)

plt.show()

# 得出来的图 --> 不满足级比检验