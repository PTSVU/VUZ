import sys

# Проверка наличия аргументов командной строки
if len(sys.argv) != 3:
    print("Usage: python replace_spaces_with_tabs.py input_file output_file")
    sys.exit(1)

input_file = sys.argv[1]  # Первый аргумент - имя входного файла
output_file = sys.argv[2]  # Второй аргумент - имя выходного файла

# Открываем входной файл для чтения
try:
    with open(input_file, 'r') as infile:
        content = infile.read()

    # Заменяем последовательности из 4 пробелов на символ табуляции
    content_with_tabs = content.replace('    ', '\t')

    # Открываем выходной файл для записи
    with open(output_file, 'w') as outfile:
        outfile.write(content_with_tabs)

    print(f"The substitution is complete. The result is saved in '{output_file}'.")
except FileNotFoundError:
    print(f"Error: File '{input_file}' was not found.")
except Exception as e:
    print(f"There's been an error: {str(e)}")

