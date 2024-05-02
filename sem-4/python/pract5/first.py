def distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между двумя точками в двумерном пространстве.

    Параметры:
    x1 (float): Координата x первой точки.
    y1 (float): Координата y первой точки.
    x2 (float): Координата x второй точки.
    y2 (float): Координата y второй точки.

    Возвращает:
    float: Расстояние между точками.

    Примеры:
    >> distance(0, 0, 3, 4)
    5.0
    >> distance(0, 0, 0, 0)
    0.0
    >> distance(1, 1, 1, 5)
    4.0
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def bucketsort(arr, k):
    """
    Сортирует массив целых чисел с использованием алгоритма Bucket Sort.

    Параметры:
    arr (list): Массив целых чисел для сортировки.
    k (int): Максимальное значение элемента в массиве.

    Возвращает:
    list: Отсортированный массив.

    Примеры:
    >> bucketsort([3, 2, 1, 5, 4], 5)
    [1, 2, 3, 4, 5]
    >> bucketsort([5, 4, 3, 2, 1], 5)
    [1, 2, 3, 4, 5]
    >> bucketsort([], 0)
    []
    """
    counts = [0] * (k + 1)
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k + 1):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


class MealyError(Exception):
    pass


class raises:
    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise AssertionError(f"{self.exception_type.__name__} not raised")
        if exc_type != self.exception_type:
            raise AssertionError(f"Expected {self.exception_type.__name__}, but got {exc_type.__name__}")
        return True


def test():
    with raises(MealyError):
        raise MealyError


if __name__ == "__main__":
    import doctest

    doctest.testmod()
