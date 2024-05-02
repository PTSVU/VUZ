def main(n):  # 3 способ
    values = [0.65, -0.62]
    for i in range(2, n + 1):
        values.append(6 * (values[i - 1] ** 2 / 2) ** 2 + values[i - 2] / 53)
    return values[n]
