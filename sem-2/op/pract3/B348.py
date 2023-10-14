# Написать функцию range_parser, которая переводит строку, задающую диапазон в соответствующий
# ему список целых чисел. Диапазон может включать в себя конструкции следующего вида
# n1-n2,n3,n4-n5:n6 (от n1 до n2 включительно, n3, от n4 до n5 включительно с шагом n6),
# конструкции могут быть разделены ',' или ', '
#
# Пример:
# range_parser("1-10,14, 20-25:2") ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]


import traceback


def range_parser(s):
    mas = []
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    s_num_a = ""
    s_num_b = ""
    ab = 0
    ren = 0
    renn = ""
    if ":" not in s and "," not in s and "-" not in s:
        mas.append(int(s))
    else:
        for i in range(len(s)):
            if s[i] == ":":
                for i1 in range(i+1, len(s)):
                    if s[i1] in nums:
                        renn += s[i1]
                        ren = int(renn)
                    if s[i1] == ",":
                        break
            if s[i] in nums and ab == 0 and s[i-1] != ":":
                s_num_a += s[i]
            if s[i] in nums and ab == 1 and s[i-1] != ":":
                s_num_b += s[i]
            if s[i] == "-":
                ab = 1
            if s[i] == "," or i == len(s)-1:
                ab = 0
                if ren == 0:
                    ren = 1
                if s_num_b == "":
                    s_num_b = s_num_a
                for i1 in range(int(s_num_a), int(s_num_b) + 1, ren):
                    mas.append(i1)
                s_num_a = ""
                s_num_b = ""
                ren = 0
                renn = ""
    return mas


# Тесты
try:
    assert range_parser("2") == [2]
    assert range_parser("5-10") == [5, 6, 7, 8, 9, 10]
    assert range_parser("1-10,14, 20-25:2") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]
    assert range_parser("1-3, 14-16,20-25:2, 26-30:3") == [1, 2, 3, 14, 15, 16, 20, 22, 24, 26, 29]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
