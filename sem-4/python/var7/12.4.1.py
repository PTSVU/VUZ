from struct import unpack_from, calcsize


class Types:
    char = "c"
    int8 = "b"
    uint8 = "B"
    int16 = "h"
    uint16 = "H"
    int32 = "i"
    uint32 = "I"
    int64 = "q"
    uint64 = "Q"
    float = "f"
    double = "d"


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream + b" "
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_a(reader):
    a1 = reader.read(Types.float)
    a2 = reader.read(Types.int16)
    a3 = [read_b(reader) for _ in range(4)]
    a4 = [reader.read(Types.int32) for _ in range(4)]
    a5 = reader.read(Types.uint32)
    a6 = reader.read(Types.uint64)
    a7 = read_c(reader)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def read_b(reader):
    b1 = reader.read(Types.float)
    b2 = reader.read(Types.uint8)
    return dict(B1=b1, B2=b2)


def read_c(reader):
    c1 = reader.read(Types.uint32)
    c2_offset = reader.read(Types.uint16)
    c2_reader = reader.jump(c2_offset)
    c2 = read_d(c2_reader)
    c3 = reader.read(Types.uint8)
    c4 = reader.read(Types.int64)
    c5_offset = reader.read(Types.uint16)
    c5_reader = reader.jump(c5_offset)
    c5 = read_e(c5_reader)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5)


def read_d(reader):
    d1 = [reader.read(Types.float) for _ in range(6)]
    d2_size = reader.read(Types.uint32)
    d2_offset = reader.read(Types.uint32)
    d2_reader = reader.jump(d2_offset)
    d2 = [d2_reader.read(Types.int32) for _ in range(d2_size)]
    d3 = [reader.read(Types.uint16) for _ in range(6)]
    d4 = reader.read(Types.double)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


def read_e(reader):
    e1 = reader.read(Types.uint16)
    e2 = reader.read(Types.int8)
    return dict(E1=e1, E2=e2)


def main(stream):
    return read_a(BinaryReader(stream, 4))
