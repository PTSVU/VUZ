import math


def a(x, y, d, e):
    ao = ((math.sqrt(math.fabs(0.25 - 2 * math.pow(y, 3))) + 4.25 * math.pow(d, 2)) / (pow((y - x), 2) + 1)) - \
        pow(e, math.fabs(4 * x - d)) * math.tan(2 * x)
    return ao


def y(x):
    a = 58
    yo = pow(2, x) + math.log(math.fabs(math.atan(x) - math.sin(a) * x)) + math.sqrt(x / (a * math.pi))
    return yo


print(a(2, 2, 2, 2), "\n\n", y(2))