# Задан список целых чисел arr и положительное число k.
# Написать функцию max_product, которая вычисляет произведение k наибольших элементов списка
#
# Пример:
# max_product([5,4,2,3],3) ==> 120


import traceback


def max_product(arr, k):
    summ = 1
    for i in range(k):
        summ = summ * max(arr)
        arr.remove(max(arr))
    return summ


# Тесты
try:
    assert max_product([10, 2, 3, 8, 1, 10, 4], 5) == 9600
    assert max_product([14, 29, -28, 39, -16, -48], 4) == -253344
    assert max_product([10, 0, -27, -1, -100], 3) == 0
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
