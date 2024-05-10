import math


def main(y, z, x):  # Способ 1
    n = 7
    sum = 0
    for i in range(1, n + 1):
        sum += 95 * abs((y[math.ceil(i / 3) - 1] / 26)
                        - 3 * x[n - math.ceil(i / 4)]
                        ** 3 - z[i - 1] ** 2) ** 3
    return 22 * sum
