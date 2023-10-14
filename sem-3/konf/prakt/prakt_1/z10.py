import os
import sys

# Проверка наличия аргумента командной строки (пути к директории)
if len(sys.argv) != 2:
    print("Usage: python find_empty_text_files.py /path/to/directory")
    sys.exit(1)

directory = sys.argv[1]  # Первый аргумент - это путь к директории

# Функция для проверки, что строка содержит только английские символы
def is_english(text):
    return all(ord(char) < 128 for char in text)

# Функция для поиска и вывода названий пустых текстовых файлов
def find_empty_text_files(directory):
    # Проверяем, что указанный путь - это директория
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    for root, _, files in os.walk(directory):
        for file_name in files:
            # Проверяем, что файл является текстовым и пустым
            if file_name.endswith(".txt") and os.path.getsize(os.path.join(root, file_name)) == 0:
                # Проверяем, что название файла состоит только из английских символов
                if is_english(file_name):
                    print(f"Empty English text file: {os.path.join(root, file_name)}")

# Вызываем функцию для поиска пустых текстовых файлов
find_empty_text_files(directory)

