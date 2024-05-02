def reverse_date(date):
    # Реверсируем дату формата "гг-мм-дд"
    parts = date.split("-")
    return "-".join(parts[::-1])


def split_email(email):
    # Разделяем информацию из ячейки email
    return [
        email.split("!")[1].split("@")[0],
        str(int(float((email.split("!")[0])) * 100)) + "%",
    ]


def shorten_name(name):
    # Сокращаем имена
    if isinstance(name, list):
        parts = name[0].split()
    else:
        parts = name.split()
    return "".join(part[0].upper() + "."
                   for part in parts[:-1]) + " " + parts[-1]


def transform_cells(table):
    # Применяем преобразования к каждой ячейке таблицы
    transformed_table = []
    for i in range(len(table)):
        transformed_table.append([None, None, None, None])
    for row in range(len(table)):
        for cell in range(len(table[row])):
            if "-" in table[row][cell]:
                transformed_table[row][cell] = (
                    reverse_date(table[row][cell]))
            elif "@" in table[row][cell]:
                transformed_table[row][cell] = (
                    split_email(table[row][cell]))[0]
                transformed_table[row][cell + 1] = (
                    split_email(table[row][cell]))[1]
            else:
                transformed_table[row][cell + 1] = (
                    shorten_name(table[row][cell]))
    return transformed_table


def transpose_table(table):
    # Транспонируем таблицу
    return [list(row) for row in zip(*table)]


def remove_empty_columns(table):
    # Удаляем пустые столбцы
    for i in table:
        for j in range(len(i) - 1):
            if i[j] is None:
                i.remove(i[j])
    return table


def remove_duplicates(table):
    # Удаляем дубликаты строк, оставляя только первое вхождение
    unique_table = []
    for row in table:
        if row not in unique_table:
            unique_table.append(row)
    return unique_table


def main(input_table):
    # Применяем все преобразования к входной таблице
    input_table = remove_empty_columns(input_table)
    input_table = remove_duplicates(input_table)
    input_table = transform_cells(input_table)
    input_table = transpose_table(input_table)
    return input_table


# Примеры входных данных
input_table1 = [
    [None, "03-09-04", "0.0!dmitrij9@mail.ru", "Дмитрий А. Цегогев"],
    [None, "99-01-28", "0.2!finibij54@rambler.ru", "Виктор Н. Финибий"],
    [None, "02-12-15", "0.3!gagasskij79@mail.ru", "Марат Е. Гагашский"],
    [None, "02-12-15", "0.3!gagasskij79@mail.ru", "Марат Е. Гагашский"],
    [None, "01-09-04", "0.7!daniel_96@yahoo.com", "Даниэль Л. Лересов"],
]

# примеры входных данных
output_table1 = [
    ['04-09-03', '28-01-99', '15-12-02', '04-09-01'],
    ['dmitrij9', 'finibij54', 'gagasskij79', 'daniel_96'],
    ['0%', '20%', '30%', '70%'],
    ['Д.А. Цегогев', 'В.Н. Финибий', 'М.Е. Гагашский', 'Д.Л. Лересов']
]


# Выполняем преобразования и выводим результаты
output_table1 = main(input_table1)
print(output_table1)
