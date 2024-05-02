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


def noise(x, y):
    return hash((hash((hash((x, y)) % 256 / 255, y)), x)) % 256 / 255


def shader(x, y):
    return noise(x, y), noise(x, y), noise(x, y)


main(shader)