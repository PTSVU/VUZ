from math import log10


def main(b: int, m: int, p: float, i=1, k=1, f=0) -> float:  # 5 способ
    if i > m:
        return f
    if k > b:
        return main(b, m, p, i + 1, 1, f)
    return main(
        b,
        m,
        p,
        i,
        k + 1,
        f + ((52 * p + 73 * k**2 + k**3) ** 3 - log10(1 + 3 * i**3) ** 4),
        )
