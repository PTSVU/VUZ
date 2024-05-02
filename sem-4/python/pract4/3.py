# Задачи 1-4, без eval и if

class Num:
    def __init__(self, value):
        self.value = value

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class PrintVisitor:
    def visit(self, node):
        try:
            return getattr(self, f"visit_{type(node).__name__}")(node)
        except AttributeError:
            return "Invalid node type"

    def visit_Num(self, node):
        return str(node.value)

    def visit_Add(self, node):
        return f"({self.visit(node.left)} + {self.visit(node.right)})"

    def visit_Mul(self, node):
        return f"({self.visit(node.left)} * {self.visit(node.right)})"


class CalcVisitor:
    def visit(self, node):
        try:
            return getattr(self, f"visit_{type(node).__name__}")(node)
        except AttributeError:
            return 0

    def visit_Num(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)


class StackVisitor:
    def visit(self, node):
        try:
            return getattr(self, f"visit_{type(node).__name__}")(node)
        except AttributeError:
            return "Invalid node type"

    def visit_Num(self, node):
        return f"PUSH {node.value}"

    def visit_Add(self, node):
        return f"{self.visit(node.left)}\n{self.visit(node.right)}\nADD"

    def visit_Mul(self, node):
        return f"{self.visit(node.left)}\n{self.visit(node.right)}\nMUL"


ast = Add(Num(7), Mul(Num(3), Num(2)))

pv = PrintVisitor()
print(pv.visit(ast))

cv = CalcVisitor()
print(cv.visit(ast))

sv = StackVisitor()
print(sv.visit(ast))