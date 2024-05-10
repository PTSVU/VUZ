def custom_sqrt(n):
    return n ** 0.5


def main(y, z, x):
    return custom_sqrt(((x ** 3 - y ** 2) ** 4) / 96 + 99 * (z + 59)) \
        - ((45 * z ** 3 - 1 - y ** 2) ** 3 + (22 - x ** 2 - y ** 3) ** 2)


print(main(-0.92, -0.87, 0.37))
print(main(-0.03, 0.59, -0.5))
print(main(-0.59, 0.79, 0.27))
print(main(-0.15, 0.31, -0.05))
print(main(0.18, -0.45, -0.87))
