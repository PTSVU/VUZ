OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}

def disasm(bytecode):
    pc = 0
    entry_printed = False
    while pc < len(bytecode):
        opcode = bytecode[pc] & 0b111
        arg = bytecode[pc] >> 3
        if arg == 0 and not entry_printed:
            print("entry:")
            entry_printed = True
        elif OP_NAMES[opcode] == 'op':
            print(f'\t{OP_NAMES[opcode]} {LIB[arg]}')
        else:
            print(f'\t{OP_NAMES[opcode]} {arg}')

        pc += 1

def not_implemented(vm):
    raise RuntimeError('Not implemented!')

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

disasm([0, 16, 16, 1, 121, 5])
