import os
import tarfile

# Функция для поиска файлов с заданным расширением и архивирования их в tar
def archive_files_with_extension(directory, extension, archive_name):
    # Проверяем, что указанный путь - это директория
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    # Создаем архив tar для записи
    with tarfile.open(archive_name, "w") as archive:
        # Рекурсивно обходим все файлы в директории
        for root, _, files in os.walk(directory):
            for file in files:
                # Проверяем, что файл имеет нужное расширение
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    # Добавляем файл в архив
                    archive.add(file_path, arcname=os.path.relpath(file_path, directory))

    print(f"Archiving is complete. Archive created '{archive_name}'.")

# Укажите путь к директории, где нужно искать файлы
search_directory = '/home/mda_m/arh'

# Укажите расширение файлов, которые нужно архивировать
file_extension = '.txt'  # Например, для текстовых файлов

# Укажите имя для создаваемого архива tar
archive_name = 'archived_files.tar'

# Вызываем функцию для архивации файлов
archive_files_with_extension(search_directory, file_extension, archive_name)

