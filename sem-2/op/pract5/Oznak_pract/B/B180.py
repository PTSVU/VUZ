# Написать функцию expanded_form, которая получает число и возвращает строку - сумму слагаемых числа.
# Между слагаемыми поставить символ +, все отделить пробелами
#
# Примеры:
# expanded_form(12345) ==> "10000 + 2000 + 300 + 40 + 5"

import traceback


def expanded_form(num):
    st_num = str(num)
    ot = ""
    for i in range(len(st_num)):
        if st_num[i] != "0":
            ot += st_num[i] + ("0" * (len(st_num) - i - 1))
        if i != len(st_num) - 1 and st_num[i+1] != "0":
            ot += " + "
    return ot


# Тесты
try:
    assert expanded_form(12345) == "10000 + 2000 + 300 + 40 + 5"
    assert expanded_form(50) == "50"
    assert expanded_form(47) == "40 + 7"
    assert expanded_form(500206) == "500000 + 200 + 6"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
