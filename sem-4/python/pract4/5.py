class SVG:
    def __init__(self):
        self.shapes = []

    def line(self, x1, y1, x2, y2, color='black'):
        self.shapes.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" />')

    def circle(self, x, y, r, color='red'):
        self.shapes.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" />')

    def save(self, filename, width, height):
        with open(filename, 'w') as f:
            f.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" ')
            f.write(f'width="{width}" height="{height}">\n')
            for shape in self.shapes:
                f.write(shape + '\n')
            f.write('</svg>')


svg = SVG()

svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('pic.svg', 100, 100)



class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0

    def draw(self, svg, x=0, y=0, dx=25, dy=50):
        self.x = x
        self.y = y
        if self.left:
            svg.line(x, y, x - dx, y + dy, color='black')
            self.left.draw(svg, x - dx, y + dy, dx, dy)
        if self.right:
            svg.line(x, y, x + dx, y + dy, color='black')
            self.right.draw(svg, x + dx, y + dy, dx, dy)
        svg.circle(x, y, r=5, color='red')


tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
tree = Tree(1, tree_2, tree_8)
t = SVG()
tree.draw(t)
t.save('tree.svg', 100, 100)