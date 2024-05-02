import tkinter as tk
import time
import threading
import queue


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


def update_image(label, shader, width, height, update_queue):
    while True:
        start_time = time.time()
        img = tk.PhotoImage(data=draw(shader, width, height)).zoom(2, 2)
        label.config(image=img)
        label.image = img
        update_queue.put("updated")
        end_time = time.time()
        elapsed_time = end_time - start_time
        fps = 1 / elapsed_time
        print(f"FPS: {fps:.2f}")


def main(shader):
    root = tk.Tk()
    root.configure(bg='black')
    label = tk.Label(root, borderwidth=0)
    label.pack()

    update_queue = queue.Queue()
    update_thread = threading.Thread(target=update_image, args=(label, shader, 256, 256, update_queue))
    update_thread.daemon = True
    update_thread.start()

    def check_update():
        if not update_queue.empty():
            update_queue.get()
            root.after(10, check_update)
        else:
            root.after(10, check_update)

    check_update()
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


def fBm(x, y, octaves=6, persistence=0.5, lacunarity=2.0):
    frequency = 1.0
    amplitude = 1.0
    total = 0.0

    for _ in range(octaves):
        total += val_noise(x * frequency, y * frequency) * amplitude
        frequency *= lacunarity
        amplitude *= persistence

    return total


def shader(x, y):
    x, y = x + time.time() / 10, y + time.time() / 10
    value = fBm(x * 5, y * 5)
    r = 1 - value
    g = 1 - value
    b = 1
    return r, g, b


main(shader)