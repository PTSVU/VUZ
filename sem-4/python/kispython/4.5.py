def main(n):  # 5 способ
    return (
        0.65
        if n == 0
        else (-0.62 if n == 1 else
              (6 * (main(n - 1) ** 2 / 2) ** 2 + main(n - 2) / 53))
    )
