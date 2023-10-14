import re

# Открываем файл для чтения
with open("hello.c", "r") as file:
    content = file.read()

# Используем регулярное выражение для поиска идентификаторов
identifiers = re.findall(r'\b\w+\b', content)

# Убираем дубликаты, используя множество (set)
unique_identifiers = set(identifiers)

# Выводим уникальные идентификаторы в консоль
for identifier in unique_identifiers:
    print(identifier)

