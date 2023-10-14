import os
import hashlib
from collections import defaultdict

# Функция для вычисления хеш-суммы файла
def calculate_file_hash(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Читаем файл блоками
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

# Функция для поиска дубликатов файлов в заданной директории
def find_duplicate_files(directory):
    file_hash_map = defaultdict(list)

    # Рекурсивно обходим все файлы в директории и её поддиректориях
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)
            file_hash_map[file_hash].append(file_path)

    # Возвращаем только те группы файлов, у которых более одного экземпляра
    return {k: v for k, v in file_hash_map.items() if len(v) > 1}

# Укажите путь к директории, в которой нужно найти дубликаты
search_directory = '/home/mda_m/dubl'

# Вызываем функцию поиска дубликатов
duplicate_files = find_duplicate_files(search_directory)

# Выводим результаты
if not duplicate_files:
    print("No duplicate files found.")
else:
    print("The following duplicate files were found:")
    for hash_value, file_list in duplicate_files.items():
        print(f"Hesh: {hash_value}")
        for file_path in file_list:
            print(f"- {file_path}")

