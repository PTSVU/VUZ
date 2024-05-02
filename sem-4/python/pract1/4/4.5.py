import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    root = tk.Tk()
    root.configure(bg='black')
    label = tk.Label(root, borderwidth=0)
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def interpolate(a, b, t):
    return a * (1 - t) + b * t


def val_noise(x, y):
    x0 = int(x)
    y0 = int(y)
    x1 = x0 + 1
    y1 = y0 + 1

    sx = x - x0
    sy = y - y0

    n00 = noise(x0, y0)
    n01 = noise(x0, y1)
    n10 = noise(x1, y0)
    n11 = noise(x1, y1)

    ix0 = interpolate(n00, n10, sx)
    ix1 = interpolate(n01, n11, sx)

    interpolated_noise = interpolate(ix0, ix1, sy)

    return interpolated_noise


def noise(x, y):
    return hash((hash((hash((x, y)) % 256 / 255, y)), x)) % 256 / 255


def shader(x, y):
    return val_noise(x * 10, y * 10), val_noise(x * 10, y * 10), val_noise(x * 10, y * 10)


main(shader)