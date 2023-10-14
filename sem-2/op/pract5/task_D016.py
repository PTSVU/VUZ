import math


def C(a, b, x, y):
    return (math.sqrt(pow(x, 2) + 1 + math.fabs(pow(a, 3) * x))) / (b * pow((2 + y), 2)) + 0.02 * math.sin(2 * y + 43)


def D(e, x, y, k):
    return pow(e, y + 1) * (pow(math.cos(k * x), 2) + 1 / math.pi * math.atan(y))


print(C(2, 2, 2, 2), "\n", D(2, 2, 2, 2))
