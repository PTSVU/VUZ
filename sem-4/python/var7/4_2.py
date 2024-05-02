def main(n):   # 2 способ
    conditions = {
        n == 0: lambda n: 0.65,
        n == 1: lambda n: -0.62
    }

    for condition, expression in conditions.items():
        if condition:
            return expression(n)

    return 6 * (main(n - 1) ** 2 / 2) ** 2 + main(n - 2) / 53
