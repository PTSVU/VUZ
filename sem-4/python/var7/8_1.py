def main(string_num):
    num = int(string_num)

    mask_3_to_0 = int('111', 2)
    mask_9_to_7 = int('0', 2)
    mask_15_to_10 = int('1111111111', 2) << 10
    mask_25_to_16 = int('1111111111111111', 2) << 16

    bits_3_to_0 = num & mask_3_to_0
    bits_9_to_7 = (num & mask_9_to_7) >> 7
    bits_15_to_10 = (num & mask_15_to_10) >> 10
    bits_25_to_16 = (num & mask_25_to_16) >> 16

    swapped_num = (((bits_3_to_0 << 7) | (bits_9_to_7 << 7))
                   | ((bits_15_to_10 << 10) | (bits_25_to_16 << 16)))

    return swapped_num
