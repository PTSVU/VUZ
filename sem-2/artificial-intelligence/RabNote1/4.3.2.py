from random import randint
import math
import matplotlib.pyplot as plt
N = 10
A = [0] * N
for i in range(N):
    A[i] = randint(1, 11)
print(A)
x = A[:5]
y = A[5:]
A1 = A
for j in range(0, 5):
    A1[j] = (math.sqrt(1 + math.e ** math.sqrt(A[j]) + math.cos(A[j] ** 2)) / (abs(1 - math.sin(A[j]) ** 3) + math.log(abs(2 * A[j]))))
    A1[j+5] = (math.sqrt(1 + math.e ** math.sqrt(A[j + 5]) + math.cos(A[j + 5] ** 2)) / (abs(1 - math.sin(A[j + 5]) ** 3) + math.log(abs(2 * A[j + 5]))))
    x[j] = (math.sqrt(1 + math.e ** math.sqrt(A[j]) + math.cos(A[j] ** 2)) / (abs(1 - math.sin(A[j]) ** 3) + math.log(abs(2 * A[j]))))
    y[j] = (math.sqrt(1 + math.e ** math.sqrt(A[j + 5]) + math.cos(A[j + 5] ** 2)) / (abs(1 - math.sin(A[j + 5]) ** 3) + math.log(abs(2 * A[j + 5]))))
plt.plot(A1)
plt.show()
plt.scatter(x, y)
#%%
