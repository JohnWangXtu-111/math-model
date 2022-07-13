import numpy as np
import matplotlib.pyplot as plt
years = np.linspace(1977, 1983, 7, dtype=np.int16)

total_incomes = np.array([18, 20, 22, 40, 44, 48, 60])
pig_incomes = np.array([10, 15, 16, 24, 38, 40, 50])
rabbit_incomes = np.array([3, 2, 12, 10, 22, 18, 20])


plt.figure()
plt.scatter(years, total_incomes)
plt.scatter(years, pig_incomes)
plt.scatter(years, rabbit_incomes)
plt.plot(years, total_incomes, label="total_income")
plt.plot(years, pig_incomes, label="pig_incomes")
plt.plot(years, rabbit_incomes, label="rabbit_incomes")
plt.legend()
plt.show()