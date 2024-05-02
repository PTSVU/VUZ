def main(n):  # 1 способ
    if n == 0:
        return 0.65
    elif n == 1:
        return -0.62
    elif n >= 2:
        return 6 * (main(n - 1) ** 2 / 2) ** 2 + main(n - 2) / 53
