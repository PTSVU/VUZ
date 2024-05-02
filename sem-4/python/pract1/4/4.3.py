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


def rotate_point(point, origin, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy


def main(shader):
    root = tk.Tk()
    root.configure(bg='black')
    label = tk.Label(root, borderwidth=0)
    img = tk.PhotoImage(data=draw(shader, 512, 512))
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    r = math.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    theta = math.atan2(y - 0.5, x - 0.5)

    mouth_angle = math.pi / 6
    eye_x, eye_y, eye_r = 0.6, 0.2, 0.09

    if ((x - eye_x)**2 + (y - eye_y)**2) < eye_r**2:
        return 0, 0, 0

    if -mouth_angle < theta < mouth_angle and r < 0.5:
        return 0, 0, 0
    elif r < 0.5:
        return 1, 1, 0
    else:
        return 0, 0, 0


main(shader)