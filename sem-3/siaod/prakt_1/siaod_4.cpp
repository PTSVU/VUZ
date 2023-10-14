#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Функция для создания текстового файла с десятичными числами
void createTextFile(const string& filename, const vector<int>& numbers) {
    ofstream file(filename);
    if (!file) {
        cerr << "Не удалось открыть файл для записи." << endl;
        return;
    }

    for (int num : numbers) {
        file << num << endl;
    }

    file.close();
}

// Функция для вывода содержимого текстового файла
void printTextFile(const string& filename) {
    ifstream file(filename);
    if (!file) {
        cerr << "Не удалось открыть файл для чтения." << endl;
        return;
    }

    string line;
    while (getline(file, line)) {
        cout << line << endl;
    }

    file.close();
}

// Функция для добавления новой записи в конец файла
void appendTextFile(const string& filename, int number) {
    ofstream file(filename, ios::app);
    if (!file) {
        cerr << "Не удалось открыть файл для добавления записи." << endl;
        return;
    }

    file << number << endl;
    file.close();
}

// Функция для чтения значения числа по его порядковому номеру в файле
int readNumberByIndex(const string& filename, int index) {
    ifstream file(filename);
    if (!file) {
        cerr << "Не удалось открыть файл для чтения." << endl;
        return -1; // Вернуть -1 в случае ошибки
    }

    int currentLine = 0;
    string line;
    while (getline(file, line)) {
        if (currentLine == index) {
            file.close();
            return stoi(line); // Преобразовать строку в число
        }
        currentLine++;
    }

    file.close();
    return -1; // Вернуть -1, если индекс выходит за пределы файла
}

// Функция для определения количества чисел в файле
int countNumbersInFile(const string& filename) {
    ifstream file(filename);
    if (!file) {
        cerr << "Не удалось открыть файл для чтения." << endl;
        return 0; // Вернуть 0 в случае ошибки
    }

    int count = 0;
    string line;
    while (getline(file, line)) {
        count++;
    }

    file.close();
    return count;
}

int main() {
    system("chcp 1251");
    const string filename = "numbers.txt";

    // Создать файл с десятичными числами
    vector<int> numbers = { 10, 20, 30, 40, 50 };
    createTextFile(filename, numbers);

    // Вывести содержимое файла
    cout << "Содержимое файла:" << endl;
    printTextFile(filename);

    // Добавить новую запись
    appendTextFile(filename, 60);

    // Прочитать значение числа по его порядковому номеру
    int index = 2; // Пример: чтение третьего числа (индекс 2)
    int value = readNumberByIndex(filename, index);
    if (value != -1) {
        cout << "Значение числа с индексом " << index << ": " << value << endl;
    }
    else {
        cout << "Число с указанным индексом не найдено." << endl;
    }

    // Определить количество чисел в файле
    int count = countNumbersInFile(filename);
    cout << "Количество чисел в файле: " << count << endl;

    return 0;
}
