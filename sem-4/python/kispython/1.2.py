def newton_sqrt(n):
    approx = n / 2
    while True:
        better = (approx + n / approx) / 2
        if abs(better - approx) < 0.00001:
            return better
        approx = better


def main(y, z, x):
    return newton_sqrt(((x ** 3 - y ** 2) ** 4) / 96 + 99 * (z + 59)) \
        - ((45 * z ** 3 - 1 - y ** 2) ** 3 + (22 - x ** 2 - y ** 3) ** 2)


print(main(-0.92, -0.87, 0.37))
print(main(-0.03, 0.59, -0.5))
print(main(-0.59, 0.79, 0.27))
print(main(-0.15, 0.31, -0.05))
print(main(0.18, -0.45, -0.87))
