from math import log10


def main(b: int, m: int, p: float) -> float:  # 2 способ
    return sum(
        ((52 * p + 73 * k**2 + k**3) ** 3 - log10(1 + 3 * i**3) ** 4)
        for i in range(1, m + 1)
        for k in range(1, b + 1)
    )
