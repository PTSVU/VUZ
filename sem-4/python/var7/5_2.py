import math


def main(y, z, x):  # Способ 2
    return 22 * sum(95 * abs((y[math.ceil(i / 3) - 1] / 26)
                             - 3 * x[7 - math.ceil(i / 4)] ** 3
                             - z[i - 1] ** 2) ** 3 for i in range(1, 8))
