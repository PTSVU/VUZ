class HTMLTag:
    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.children = []

    def __enter__(self):
        print(f'<{self.tag_name}>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for child in self.children:
            print(child)
        print(f'</{self.tag_name}>')

    def add_child(self, child):
        self.children.append(child)

    def __call__(self, *args, **kwargs):
        if args:
            self.children.append(args[0])
        return self

    def __repr__(self):
        return f'<{self.tag_name}>{" ".join(map(str, self.children))}</{self.tag_name}>'


class HTML:
    def __init__(self):
        self.body = HTMLTag('body')

    def get_code(self):
        with self.body as b:
            with HTMLTag('div') as d1:
                d1(HTMLTag('p')('line 1.'))
                d1(HTMLTag('p')('line 2.'))
            with HTMLTag('div') as d2:
                d2(HTMLTag('p')('line 3.'))


html = HTML()
html.get_code()
