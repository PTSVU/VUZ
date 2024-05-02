from math import tan, atan, floor


def main(z: int) -> float:  # 1 способ
    if z < 78:
        return 1 + tan(z) ** 6
    elif 78 <= z < 111:
        return (atan(z) + ((23 * z - 84 * z ** 2 - 97) ** 7 / 61)) \
            + 75 * z ** 3
    elif 111 <= z < 192:
        return 49 * z ** 5 - z ** 6 - z ** 7
    else:
        return z ** 3
