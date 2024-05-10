from math import tan, atan, floor


def main(z: int) -> float:  # 3 способ
    conditions = {
        z < 78: lambda z: 1 + tan(z) ** 6,
        78
        <= z
        < 111: lambda z: (atan(z) + ((23 * z - 84 * z**2 - 97) ** 7 / 61))
                         + 75 * z**3,
        111 <= z < 192: lambda z: 49 * z**5 - z**6 - z**7,
    }

    for condition, expression in conditions.items():
        if condition:
            return expression(z)

    return z**3
