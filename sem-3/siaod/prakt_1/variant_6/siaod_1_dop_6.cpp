#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main() {
    system("chcp 1251");
    const string inputFilename = "input.txt";
    const string outputFilename = "output.txt";

    ifstream inputFile(inputFilename);
    if (!inputFile) {
        cerr << "Не удалось открыть исходный файл для чтения." << endl;
        return 1;
    }

    vector<int> numbers;
    int number;
    while (inputFile >> number) {
        numbers.push_back(number);
    }

    inputFile.close();

    if (numbers.empty()) {
        cerr << "Исходный файл не содержит чисел." << endl;
        return 1;
    }

    int sum = numbers[0] + numbers[numbers.size() - 1];

    ofstream outputFile(outputFilename);
    if (!outputFile) {
        cerr << "Не удалось создать файл для записи." << endl;
        return 1;
    }

    for (int num : numbers) {
        int result = num * sum;
        outputFile << result << endl;
    }

    outputFile.close();

    cout << "Файл " << outputFilename << " успешно создан с умноженными значениями." << endl;

    return 0;
}