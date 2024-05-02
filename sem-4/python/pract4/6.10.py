class Compiler:
    def __init__(self):
        self.bytecode = []

    def compile(self, source_code):
        tokens = source_code.split()
        for token in tokens:
            if token.isdigit():
                self.bytecode.append((0, int(token)))  # push
            elif token in ['+', '-', '*', '/', '%', '&', '|', '^', '<', '>', '=', '<<', '>>']:
                op = ['+', '-', '*', '/', '%', '&', '|', '^', '<', '>', '=', '<<', '>>'].index(token)
                self.bytecode.append((1, op))  # op
            elif token == '.':
                self.bytecode.append((1, 17))  # print
            elif token == 'exit':
                self.bytecode.append((5, 0))  # exit
            else:
                raise ValueError(f"Unknown token: {token}")

        entry_point = len(self.bytecode)
        self.bytecode.insert(0, entry_point)  # Insert entry point at the beginning
        return self.bytecode

# Тестирование компилятора
compiler = Compiler()
bytecode = compiler.compile("2 2 + . exit")
print(bytecode)  # Выведет: [6, (0, 2), (0, 2), (1, 0), (1, 17), (5, 0)]
