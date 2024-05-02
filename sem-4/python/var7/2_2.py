from math import tan, atan, floor


def main(z):  # 2 способ
    return (1 + tan(z) ** 6 if z < 78 else
            ((atan(z) + ((23 * z - 84 * z ** 2 - 97) ** 7 / 61))
                + 75 * z ** 3 if 78 <= z < 111 else
                (49 * z ** 5 - z ** 6 - z ** 7
                    if 111 <= z < 192 else
                    z ** 3)))
