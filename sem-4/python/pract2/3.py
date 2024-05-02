# 3.1. Преобразовать элементы списка s из строковой в числовую форму:
s = ['1', '2', '3']; result = list(map(int, s))
print("3.1.: ", result)

# 3.2. Подсчитать количество различных элементов в последовательности s:
s = [1, 2, 3, 1, 2, 3, 4, 5]; result = len(set(s))
print("3.2.: ", result)

# 3.3. Обратить последовательность s без использования функций:
s = [1, 2, 3, 4, 5]; result = s[::-1]
print("3.3.: ", result)

# 3.4. Выдать список индексов, на которых найден элемент x в последовательности s:
s = [1, 2, 3, 4, 1, 2, 1, 5]; x = 1; result = [i for i, val in enumerate(s) if val == x]
print("3.4.: ", result)

# 3.5. Сложить элементы списка s с четными индексами:
s = [1, 2, 3, 4, 5]; result = sum(s[::2])
print("3.5.: ", result)

# 3.6. Найти строку максимальной длины в списке строк s:
s = ['aaa', 'bb', 'ccc', 'dddd']; result = max(s, key=len)
print("3.6.: ", result)

# 3.7. Проверить, относится ли число к числам харшад (делящиеся нацело на сумму своих цифр):
n = 18; result = n % sum(map(int, str(n))) == 0
print("3.7.: ", result)

# 3.8. Сгенерировать случайную текстовую строку с заданным максимальным размером:
import random; import string; max_length = 10; result = ''.join(random.choices(string.ascii_letters + string.digits, k=max_length))
print("3.8.: ", result)

# 3.9. Реализовать функцию-однострочник для RLE-сжатия:
from itertools import groupby; result = [(char, len(list(group))) for char, group in groupby('ABBCCCDEF')]
print("3.9.: ", result)
