# Написать функцию blocks, которая получает строку, состоящую из букв и цифр и возвращает строку в виде блоков,
# разделенных символом дефис. Элементы блока должны быть отсортированы по принципу, указанному ниже, и
# каждый блок не может содержать несколько экземпляров одного и того же символа.
# Порядок блоков:
# строчные буквы (a - z) в алфавитном порядке
# заглавные буквы (A - Z) в алфавитном порядке
# цифры (0 - 9) в порядке возрастания
#
#
# Примеры:
# blocks("21AxBz") ==> "xzAB12"
# blocks("abacad") ==> "abcd-a-a"

import traceback


def blocks(s):
    ct_alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]
    bi_alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    temp_ct = ""
    temp_bi = ""
    temp_num = ""
    temp_sf = ""
    temp_sff = ""
    ot = ""
    for i in range(len(s)):
        if s[i] in ct_alf:
            if s[i] in temp_ct:
                temp_sf += s[i]
            else:
                temp_ct += s[i]
        if s[i] in bi_alf:
            if s[i] in temp_bi:
                temp_sf += s[i]
            else:
                temp_bi += s[i]
        if s[i] in nums:
            if s[i] in temp_num:
                temp_sf += s[i]
            else:
                temp_num += s[i]
    temp_num = ''.join(sorted(temp_num))
    ot += ''.join(sorted(temp_ct) + sorted(temp_bi) + sorted(temp_num))
    temp_sf = sorted(temp_sf)
    while(True):
        temp_ct = ""
        temp_bi = ""
        temp_num = ""
        for i in range(len(temp_sf)):
            if temp_sf[i] in ct_alf:
                if temp_sf[i] in temp_ct:
                    temp_sff += temp_sf[i]
                else:
                    temp_ct += temp_sf[i]
            if temp_sf[i] in bi_alf:
                if temp_sf[i] in temp_bi:
                    temp_sff += temp_sf[i]
                else:
                    temp_bi += temp_sf[i]
            if temp_sf[i] in nums:
                if temp_sf[i] in temp_num:
                    temp_sff += temp_sf[i]
                else:
                    temp_num += temp_sf[i]
        ot += "-" + ''.join(sorted(temp_ct) + sorted(temp_bi) + sorted(temp_num))
        if temp_sff != "":
            temp_sf = temp_sff
            temp_sff = ""
        else:
            break
    if ot[-1] == "-":
        ot = ot[:-1]
    return ot

# Тесты
try:
    assert blocks("21AxBz") == "xzAB12"
    assert blocks("abacad") == "abcd-a-a"
    assert blocks("heyitssampletestkk") == "aehiklmpsty-ekst-est"
    assert blocks("6zjX9qcwTIuYNvdmL3CtElHa2n0rogKsSVPRWG4QAMUOe8JkyfxZDiBpb1Fh75GUTLMcbio7HO6rvn1NtDRmPJAejuXVFgaZI3pK90s4fBzqwEd5yWCQh8Sl2kxY") == \
           "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")