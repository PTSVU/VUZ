from math import log10


def main(b, m, p):  # 4 способ
    f = 0
    i = 1
    while i <= m:
        k = 1
        while k <= b:
            f += (52 * p + 73 * k**2 + k**3) ** 3 - log10(1 + 3 * i**3) ** 4
            k += 1
        i += 1
    return f
