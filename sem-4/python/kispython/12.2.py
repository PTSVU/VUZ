from struct import unpack_from, calcsize



Types = {
    'char': "c",
    'int8': "b",
    'uint8': "B",
    'int16': "h",
    'uint16': "H",
    'int32': "i",
    'uint32': "I",
    'int64': "q",
    'uint64': "Q",
    'float': "f",
    'double': "d"
}


def read(stream, offset, order, pattern):
    size = calcsize(pattern)
    data = unpack_from(order + pattern, stream, offset)
    return data[0], offset + size


def read_a(stream, offset, order):
    a1, offset = read(stream, offset, order, Types['float'])
    a2, offset = read(stream, offset, order, Types['int16'])
    a3 = [read_b(stream, offset + i * calcsize(
        Types['float'] + Types['uint8']), order) for i in range(4)]
    offset += 4 * calcsize(Types['float'] + Types['uint8'])
    a4 = [read(stream, offset + i * 4, order, Types['int32']
               )[0] for i in range(4)]
    a5, offset = read(stream, offset + 4 * 4, order, Types['uint32'])
    a6, offset = read(stream, offset, order, Types['uint64'])
    a7 = read_c(stream, offset, order)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7), offset


def read_b(stream, offset, order):
    b1, offset = read(stream, offset, order, Types['float'])
    b2, offset = read(stream, offset, order, Types['uint8'])
    return dict(B1=b1, B2=b2)


def read_c(stream, offset, order):
    c1, offset = read(stream, offset, order, Types['uint32'])
    c2_offset, offset = read(stream, offset, order, Types['uint16'])
    c2, _ = read_d(stream, c2_offset, order)
    c3, offset = read(stream, offset, order, Types['uint8'])
    c4, offset = read(stream, offset, order, Types['int64'])
    c5_offset, offset = read(stream, offset, order, Types['uint16'])
    c5, _ = read_e(stream, c5_offset, order)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5)


def read_d(stream, offset, order):
    d1 = [read(stream, offset + i * 4, order, Types['float']
               )[0] for i in range(6)]
    offset += 6 * 4
    d2_size, offset = read(stream, offset, order, Types['uint32'])
    d2_offset, offset = read(stream, offset, order, Types['uint32'])
    d2 = [read(stream, d2_offset + i * 4, order, Types['int32']
               )[0] for i in range(d2_size)]
    d3 = [read(stream, offset + i * 2, order, Types['uint16']
               )[0] for i in range(6)]
    offset += 6 * 2
    d4, offset = read(stream, offset, order, Types['double'])
    return dict(D1=d1, D2=d2, D3=d3, D4=d4), offset


def read_e(stream, offset, order):
    e1, offset = read(stream, offset, order, Types['uint16'])
    e2, offset = read(stream, offset, order, Types['int8'])
    return dict(E1=e1, E2=e2), offset


def main(stream):
    order = "<"  # You can set the desired byte order here
    offset = 4  # Assuming the offset starts at 4
    return read_a(stream, offset, order)[0]


print(main((b'RCJ\xd5;\x824?\xd7\xfc\xccPF\xbf\xa3&\x8fp?\x06\x95\x8e\xe3\xbe\x08\x85NB'
            b'\xbf\x18\x8f^\xd0\xdb\xff1\x0b\x1a\xb0\xd0l^\x18\xbf\xfd\xc5\xb1\xf0'
            b':\xae\xa0\x02xZ;[\xd1\xf6d\xe9\xaa\xadS\x00N\x140`C\r\x11W+\x87\x00`'
            b'\xa6\x88E\x8b\xab\x844\xabG\x19?d\x8dz?z\xc4|\xbf\xbaT\xff>\x10\x8a\xa6<\xb2'
            b'\x8fh\xbf\x02\x00\x00\x00K\x00\x00\x00\xb1/\xee\x05$U\x14lxE\x80BTj\xae9N'
            b'g\xda?\xbc\xbc\xdf')))
