import math


def main(y, z, x):  # Сбособ 3
    n = 7
    sum_val = 0
    i = 1
    while i <= n:
        sum_val += 95 * abs((y[math.ceil(i / 3) - 1] / 26)
                            - 3 * x[n - math.ceil(i / 4)] ** 3
                            - z[i - 1] ** 2) ** 3
        i += 1
    return 22 * sum_val
