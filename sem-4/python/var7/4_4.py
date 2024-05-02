def main(n):  # 4 способ
    match n:
        case 0:
            return 0.65
        case 1:
            return -0.62
        case _:
            return 6 * (main(n - 1) ** 2 / 2) ** 2 + main(n - 2) / 53
