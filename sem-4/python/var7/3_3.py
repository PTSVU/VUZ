from functools import reduce
from math import log10


def main(b: int, m: int, p: float) -> float:  # 3 способ
    return reduce(
        lambda acc, i: acc
        + reduce(
            lambda acc_inner, k: acc_inner
                                 + ((52 * p + 73 * k ** 2 + k ** 3) ** 3 - log10(1 + 3 * i ** 3) ** 4),
            range(1, b + 1),
            0,
        ),
        range(1, m + 1),
        0,
    )
