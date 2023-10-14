# Написать функцию strong_number(number), которая определяет является ли число сильным.
# Число сильное, если сумма факториалов цифр числа равна самому числу.
#
# Примеры:
# strong_number(145) => True -> 1! + 4! + 5! = 1 + 24 + 120 = 145

import traceback
import math


def strong_number(number):
    summ = 0
    str_num = str(number)
    for i in range(len(str_num)):
        summ = summ + math.factorial(int(str_num[i]))
    return summ == number


# Тесты
try:
    assert strong_number(1) == True
    assert strong_number(2) == True
    assert strong_number(7) == False
    assert strong_number(93) == False
    assert strong_number(145) ==  True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")