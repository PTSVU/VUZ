import math


def main(y, z, x, n=7, i=1, sum=0):  # Способ 4
    if i > n:
        return 22 * sum
    else:
        sum += 95 * abs((y[math.ceil(i / 3) - 1] / 26)
                        - 3 * x[n - math.ceil(i / 4)] ** 3
                        - z[i - 1] ** 2) ** 3
        return main(y, z, x, n, i + 1, sum)
