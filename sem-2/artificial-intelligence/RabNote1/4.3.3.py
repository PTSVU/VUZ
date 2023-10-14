import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz
x = np.arange(1, 9, 0.1)        #параметры графика
y = np.abs(np.cos(x * (np.e ** np.cos(x) + np.log(x + 1))))     #функиця
plt.grid()      #сетка графика
plt.plot(x, y, c = "black")     #создаем саму функцию, линия разделяющая график-черная
plt.fill_between(x, y)      #покраска области под графиком
area = trapz(y)     #функция вычисления подинтегрального простарнства
print(area)
#%%
