#!/bin/bash

# Проверка наличия аргумента командной строки
if [ $# -eq 0 ]; then
    echo "Usage: $0 'your text here'"
    exit 1
fi

text="$1"
length=${#text}

# Определение ширины баннера
width=$((length + 4))

# Вывод верхней границы
printf "+"
for ((i = 0; i < width - 2; i++)); do
    printf "-"
done
printf "+\n"

# Вывод текста в баннере
printf "| %s |\n" "$text"

# Вывод нижней границы
printf "+"
for ((i = 0; i < width - 2; i++)); do
    printf "-"
done
printf "+\n"

