import os

# Список расширений файлов, которые нужно проверить
extensions_to_check = ['.c', '.js', '.py']

# Функция для проверки наличия комментария в первой строке файла
def check_comment_in_first_line(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        if first_line.startswith('//') or first_line.startswith('#'):
            return True
        elif first_line.startswith('/*'):
            return True
    return False

# Функция для поиска файлов с заданными расширениями и проверки комментариев
def search_and_check_comments(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_extension = os.path.splitext(file_name)[1]
            if file_extension in extensions_to_check:
                if check_comment_in_first_line(file_path):
                    print(f"File: {file_path} - has a comment in the first line.")

# Укажите директорию, в которой вы хотите выполнить поиск
search_directory = '/home'

search_and_check_comments(search_directory)

