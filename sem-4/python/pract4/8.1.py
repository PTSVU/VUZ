from pathlib import Path
import tkinter as tk

SCALE_X = 6
SCALE_Y = 4

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]

def draw_line(coords, color_index):
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)

def fill_area(coords, color_index):
    canvas.create_polygon(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                          fill='#%02x%02x%02x' % COLORS[color_index])

def draw(pic):
    # TODO: Implement the drawing logic
    pass

pic = Path('data/PIC.1').read_bytes()
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()
