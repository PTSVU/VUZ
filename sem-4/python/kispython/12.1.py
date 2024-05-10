from struct import unpack_from, calcsize


def main(stream):
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

    order = "<"  # You can set the desired byte order here
    offset = 4  # Assuming the offset starts at 4

    size = calcsize(Types['float'])
    a1 = unpack_from(order + Types['float'], stream, offset)[0]
    offset += size

    size = calcsize(Types['int16'])
    a2 = unpack_from(order + Types['int16'], stream, offset)[0]
    offset += size

    a3 = []
    for i in range(4):
        sub_offset = offset + i * (calcsize(Types['float']) + calcsize(Types['uint8']))
        b1 = unpack_from(order + Types['float'], stream, sub_offset)[0]
        b2 = unpack_from(order + Types['uint8'], stream, sub_offset + calcsize(Types['float']))[0]
        a3.append({'B1': b1, 'B2': b2})

    offset += 4 * (calcsize(Types['float']) + calcsize(Types['uint8']))

    a4 = []
    for i in range(4):
        sub_offset = offset + i * calcsize(Types['int32'])
        a4.append(unpack_from(order + Types['int32'], stream, sub_offset)[0])

    offset += 4 * calcsize(Types['int32'])

    size = calcsize(Types['uint32'])
    a5 = unpack_from(order + Types['uint32'], stream, offset)[0]
    offset += size

    size = calcsize(Types['uint64'])
    a6 = unpack_from(order + Types['uint64'], stream, offset)[0]
    offset += size

    c1 = unpack_from(order + Types['uint32'], stream, offset)[0]
    offset += calcsize(Types['uint32'])

    c2_offset = unpack_from(order + Types['uint32'], stream, offset)[0]
    offset += calcsize(Types['uint32'])

    d1 = []
    for i in range(6):
        sub_offset = c2_offset + i * calcsize(Types['float'])
        d1.append(unpack_from(order + Types['float'], stream, sub_offset)[0])

    d2_size = unpack_from(order + Types['uint32'], stream, offset)[0]
    offset += calcsize(Types['uint32'])

    d2_offset = unpack_from(order + Types['uint32'], stream, offset)[0]
    offset += calcsize(Types['uint32'])

    d2 = []
    for i in range(d2_size):
        sub_offset = d2_offset + i * calcsize(Types['int32'])
        d2.append(unpack_from(order + Types['int32'], stream, sub_offset)[0])

    d3 = []
    for i in range(6):
        sub_offset = offset + i * calcsize(Types['uint16'])
        d3.append(unpack_from(order + Types['uint16'], stream, sub_offset)[0])

    offset += 6 * calcsize(Types['uint16'])

    d4 = unpack_from(order + Types['double'], stream, offset)[0]

    e1 = unpack_from(order + Types['uint16'], stream, offset)[0]
    e2 = unpack_from(order + Types['int8'], stream, offset + calcsize(Types['uint16']))[0]

    return {
        'A1': a1,
        'A2': a2,
        'A3': a3,
        'A4': a4,
        'A5': a5,
        'A6': a6,
        'A7': {
            'C1': c1,
            'C2': {
                'D1': d1,
                'D2': d2,
                'D3': d3,
                'D4': d4
            },
            'C3': unpack_from(order + Types['uint8'], stream, offset)[0],
            'C4': unpack_from(order + Types['int64'], stream, offset + calcsize(Types['uint8']))[0],
            'C5': {
                'E1': e1,
                'E2': e2
            }
        }
    }


print(main((b'RCJ\xd5;\x824?\xd7\xfc\xccPF\xbf\xa3&\x8fp?\x06\x95\x8e\xe3\xbe\x08\x85NB'
            b'\xbf\x18\x8f^\xd0\xdb\xff1\x0b\x1a\xb0\xd0l^\x18\xbf\xfd\xc5\xb1\xf0'
            b':\xae\xa0\x02xZ;[\xd1\xf6d\xe9\xaa\xadS\x00N\x140`C\r\x11W+\x87\x00`'
            b'\xa6\x88E\x8b\xab\x844\xabG\x19?d\x8dz?z\xc4|\xbf\xbaT\xff>\x10\x8a\xa6<\xb2'
            b'\x8fh\xbf\x02\x00\x00\x00K\x00\x00\x00\xb1/\xee\x05$U\x14lxE\x80BTj\xae9N'
            b'g\xda?\xbc\xbc\xdf')))
