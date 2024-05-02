import pytest
from first import bucketsort


# 2.1
@pytest.fixture
def unsorted_list():
    return [3, 1, 4, 1, 5, 9, 2, 6]


@pytest.fixture
def sorted_list():
    return [1, 1, 2, 3, 4, 5, 6, 9]


def test_bucketsort_sorted(unsorted_list, sorted_list):
    assert bucketsort(unsorted_list, 10) == sorted_list


def test_bucketsort_empty():
    assert bucketsort([], 0) == []


def test_bucketsort_single():
    assert bucketsort([42], 43) == [42]


test_bucketsort_empty()
test_bucketsort_single()
test_bucketsort_sorted(unsorted_list(), sorted_list())

# 2.2
# Программа с ошибкой
def get_user_input():
    return input("Введите число: ")


def process_input():
    user_input = get_user_input()
    try:
        number = int(user_input)
        return f"Вы ввели число {number}"
    except ValueError:
        return "Ошибка: введите целое число"


# Макетный тест
def test_process_input(monkeypatch):
    # Подменяем ввод пользователя
    monkeypatch.setattr('builtins.input', lambda _: "42")
    assert process_input() == "Вы ввели число 42"
