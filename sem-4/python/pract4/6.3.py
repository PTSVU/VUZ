def emit(vm):
    char_code = vm.stack.pop()
    print(chr(char_code), end='')

LIB = {
    '+': lambda vm: vm.stack.append(vm.stack.pop() + vm.stack.pop()),
    '-': lambda vm: vm.stack.append(-vm.stack.pop() + vm.stack.pop()),
    '*': lambda vm: vm.stack.append(vm.stack.pop() * vm.stack.pop()),
    '/': lambda vm: vm.stack.append(1 // vm.stack.pop() * vm.stack.pop()),
    '%': lambda vm: vm.stack.append(vm.stack.pop() % vm.stack.pop()),
    '&': lambda vm: vm.stack.append(vm.stack.pop() & vm.stack.pop()),
    '|': lambda vm: vm.stack.append(vm.stack.pop() | vm.stack.pop()),
    '^': lambda vm: vm.stack.append(vm.stack.pop() ^ vm.stack.pop()),
    '<': lambda vm: vm.stack.append(vm.stack.pop() < vm.stack.pop()),
    '>': lambda vm: vm.stack.append(vm.stack.pop() > vm.stack.pop()),
    '=': lambda vm: vm.stack.append(vm.stack.pop() == vm.stack.pop()),
    '<<': lambda vm: vm.stack.append(vm.stack.pop() << vm.stack.pop()),
    '>>': lambda vm: vm.stack.append(vm.stack.pop() >> vm.stack.pop()),
    'if': lambda vm: vm.stack.pop() if vm.stack.pop() else None,
    'for': lambda vm: [vm.stack.pop() for _ in range(vm.stack.pop())],
    '.': emit,
    '?': NotImplemented,
    'array': NotImplemented,
    '@': NotImplemented,
    '!': NotImplemented
}

OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}

class VM:
    def __init__(self, code):
        self.stack = []
        self.code = code
        self.scope = {}

    def run(self):
        pc = self.code[0]
        while pc < len(self.code):
            opcode = self.code[pc] & 0b111
            arg = self.code[pc] >> 3
            if OP_NAMES[opcode] == 'push':
                self.stack.append(arg)
            elif OP_NAMES[opcode] == 'op':
                LIB[arg](self)
            elif OP_NAMES[opcode] == 'exit':
                break
            elif OP_NAMES[opcode] == 'is':
                function_address = self.stack.pop()
                self.scope[arg] = ('function', function_address)
            elif OP_NAMES[opcode] == 'call':
                func_info = self.scope[arg]
                if func_info[0] == 'function':
                    func_address = func_info[1]
                    self.stack.append(pc + 1)
                    pc = func_address
                else:
                    raise RuntimeError('Attempting to call a non-function')
            pc += 1

def not_implemented(vm):
    raise RuntimeError('Not implemented!')

# Пример использования
bytecode = [57, 8440, 129, 8704, 129, 8688, 129, 8600, 129, 8704, 129, 8576, 129, 8672,
            129, 8672, 129, 8576, 129, 256, 129, 8728, 129, 8712, 129, 8696, 129, 8616,
            129, 8768, 129, 8680, 129, 8688, 129, 256, 129, 8592, 129, 8792, 129, 8696,
            129, 8688, 129, 8664, 129, 8680, 129, 8616, 129, 8680, 129, 8576, 129, 264,
            129, 5, 0, 3, 2, 5]

vm = VM(bytecode)
vm.run()
