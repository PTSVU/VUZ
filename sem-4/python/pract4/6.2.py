class VM:
    def __init__(self, code):
        self.stack = []
        self.code = code

    def run(self):
        pc = 0
        while pc < len(self.code):
            opcode = self.code[pc] & 0b111
            arg = self.code[pc] >> 3

            if opcode == 0:  # push
                self.stack.append(arg)
            elif opcode == 1:  # op
                operation = LIB[arg]
                if operation == '+':
                    a, b = self.stack.pop(), self.stack.pop()
                    self.stack.append(a + b)
                # Добавьте другие операции (вычитание, умножение и т. д.)
            elif opcode == 5:  # exit
                break

            pc += 1

LIB = [
    '+',
    '-',
    '*',
    '/',
    '%',
    '&',
    '|',
    '^',
    '<',
    '>',
    '=',
    '<<',
    '>>',
    'if',
    'for',
    '.',
    'emit',
    '?',
    'array',
    '@',
    '!'
]

# Пример использования
bytecode = [0, 16, 16, 1, 121, 5]
vm = VM(bytecode)
vm.run()
print("Результат:", vm.stack[-1])  # Выводим результат
