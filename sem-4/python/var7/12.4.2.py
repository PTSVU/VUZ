from struct import unpack_from, calcsize
from typing import Dict, Any


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
        self.stream = stream + b""
        self.offset = offset
        self.order = order

    def jump(self, offset):
        return BinaryReader(self.stream, offset, self.order)

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_a(reader: BinaryReader) -> Dict[str, Any]:
    return {
        "A1": reader.read(Types.float),
        "A2": reader.read(Types.int16),
        "A3": [read_b(reader) for _ in range(4)],
        "A4": [reader.read(Types.int32) for _ in range(4)],
        "A5": reader.read(Types.uint32),
        "A6": reader.read(Types.uint64),
        "A7": read_c(reader)
    }


def read_b(reader: BinaryReader) -> Dict[str, Any]:
    return {
        "B1": reader.read(Types.float),
        "B2": reader.read(Types.uint8)
    }


def read_c(reader: BinaryReader) -> Dict[str, Any]:
    c1 = reader.read(Types.uint32)
    c2_offset = reader.read(Types.uint16)
    c2 = read_d(reader.jump(c2_offset))
    c3 = reader.read(Types.uint8)
    c4 = reader.read(Types.int64)
    c5_offset = reader.read(Types.uint16)
    c5 = read_e(reader.jump(c5_offset))
    return {
        "C1": c1,
        "C2": c2,
        "C3": c3,
        "C4": c4,
        "C5": c5
    }


def read_d(reader: BinaryReader) -> Dict[str, Any]:
    d1 = [reader.read(Types.float) for _ in range(6)]
    d2_size = reader.read(Types.uint32)
    d2_offset = reader.read(Types.uint32)
    d2_reader = reader.jump(d2_offset)
    d2 = [d2_reader.read(Types.int32) for _ in range(d2_size)]
    d3 = [reader.read(Types.uint16) for _ in range(6)]
    d4 = reader.read(Types.double)
    return {
        "D1": d1,
        "D2": d2,
        "D3": d3,
        "D4": d4
    }


def read_e(reader: BinaryReader) -> Dict[str, Any]:
    return {
        "E1": reader.read(Types.uint16),
        "E2": reader.read(Types.int8)
    }


def main(stream: bytes) -> Dict[str, Any]:
    return read_a(BinaryReader(stream, 4))


x1 = (
    b"RCJ\xd5;\x824?\xd7\xfc\xccPF\xbf\xa3&\x8fp?\x06\x95\x8e\xe3\xbe\x08\x85NB"
    b"\xbf\x18\x8f^\xd0\xdb\xff1\x0b\x1a\xb0\xd0l^\x18\xbf\xfd\xc5\xb1\xf0"
    b":\xae\xa0\x02xZ;[\xd1\xf6d\xe9\xaa\xadS\x00N\x140`C\r\x11W+\x87\x00`"
    b"\xa6\x88E\x8b\xab\x844\xabG\x19?d\x8dz?z\xc4|\xbf\xbaT\xff>\x10\x8a\xa6<\xb2"
    b"\x8fh\xbf\x02\x00\x00\x00K\x00\x00\x00\xb1/\xee\x05$U\x14lxE\x80BTj\xae9N"
    b"g\xda?\xbc\xbc\xdf"
)

x2 = (
    b"RCJ\xd5\xa3\x84'\xbf\x98\r\xbci\xea\xbe\x91\x1a\xd0\x1c?`\xb7\xc7Z\xbf"
    b'L@c\xda>\xe4 \xbd\xc6\xf0@j\xa1\x1e\xc6\x07w\x83)\xf4\xde\x9b>"v]\xc7\xa6'
    b"6T\xe0B\xa3\xc4O\xe46\xa3S\x00q\xe0\xa4\x1e&\xd1\x9fm`\x87\x00~k2\xf5\x8c"
    b"\xe8\xcb\xd7\x87\x7f\x10\xbf\xe4\xae\xf1>\xe5\xdd\xaa>\xc2Y\xc2=\x98"
    b"\xe2a\xbf\xbf:\x12\xbf\x02\x00\x00\x00K\x00\x00\x00<y1\x16\xff\xa4\xc3\xf9L"
    b"\xfa\xf1:p\x13o\x87|w\xbc?\x1fb\x8a"
)

# Вызов функции main и вывод результатов
result1 = main(x1)
print(result1)

result2 = main(x2)
print(result2)
