import math
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


def circle_sdf(x, y, center_x, center_y, radius):
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    return distance - radius


def square_sdf(x, y, center_x, center_y, size):
    dx = abs(x - center_x) - size
    dy = abs(y - center_y) - size
    return max(dx, dy)


def rectangle_sdf(x, y, center_x, center_y, width, height):
    dx = abs(x - center_x) - width
    dy = abs(y - center_y) - height
    return max(dx, dy)


def union(a, b):
    return min(a, b)


def intersect(a, b):
    return max(a, b)


def difference(a, b):
    return max(a, -b)


def sdf_func(x, y):
    circle1 = circle_sdf(x, y, 0.5, 0.3, 0.2)
    circle2 = circle_sdf(x, y, 0.5, 0.3, 0.1)
    rectangle1 = rectangle_sdf(x, y, 0.3, 0.5, 0.1, 0.4)
    return union(difference(circle1, circle2), rectangle1)


def shader(x, y):
    d = sdf_func(x, y)
    return d > 0, abs(d) * 3, 0


main(shader)