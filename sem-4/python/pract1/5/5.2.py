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
    img = tk.PhotoImage(data=draw(shader, 1024, 1024))
    label.pack()
    label.config(image=img)
    tk.mainloop()


def sdf_func(x, y):
    center_x, center_y, size = 0.5, 0.5, 0.4
    dx = abs(x - center_x) - size
    dy = abs(y - center_y) - size
    return max(dx, dy)


def shader(x, y):
    d = sdf_func(x, y)
    return d > 0, abs(d) * 3, 0


main(shader)