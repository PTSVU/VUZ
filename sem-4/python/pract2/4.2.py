from ctypes import *


def decrypt(v, k):
    v0, v1 = c_uint32(v[0]), c_uint32(v[1])
    sum = 0xC6EF3720
    delta = 0x9E3779B9
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

    for i in range(32):
        v1.value -= ((v0.value << 4) + k2) ^ (v0.value + sum) ^ ((v0.value >> 5) + k3)
        v0.value -= ((v1.value << 4) + k0) ^ (v1.value + sum) ^ ((v1.value >> 5) + k1)
        sum -= delta

    return v0.value, v1.value


cipher_text = [
    0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
    0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
    0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
    0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
    0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
    0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
    0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
    0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
    0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
    0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637
]

key = [0x0, 0x4, 0x5, 0x1]
for i in range(0, len(cipher_text), 2):
    cipher_text[i:i + 2] = decrypt(cipher_text[i:i + 2], key)

print("Расшифрованное сообщение:")
for i in cipher_text:
    print(chr(i), end='')
