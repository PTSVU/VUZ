"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""
import string
def wiki_function():
    file_name = "B436_a.txt"
    with open(file_name, "r") as f:
        lines = f.readlines()

    words = []
    for line in lines:
        if line.strip():
            line = line.translate(str.maketrans('', '', string.digits+string.punctuation))
            words += line.lower().split()

    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i, (word, count) in enumerate(sorted_word_count[:10], start=1):
        print(f"{i} place --- {word} --- {count} times")

    popular_words = [word for word, _ in sorted_word_count[:10]]
    new_text = ' '.join(["PYTHON" if word in popular_words else word for word in words])


    with open("B436_b.txt", "w") as f:
        start_index = 0
        while start_index < len(new_text):
            end_index = start_index + 100
            if end_index >= len(new_text):
                end_index = len(new_text)
            else:
                while new_text[end_index] != ' ':
                    end_index -= 1

            f.write(new_text[start_index:end_index]+'\n')
            start_index = end_index


# Вызов функции
wiki_function()