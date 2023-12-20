#include "shannon_fano.h"
#include "huffman.h"
#include "lz77.h"
#include "lz78.h"
#include <iostream>
#include <vector>

int main() {
    setlocale(LC_ALL, "rus");
    // Задание 1: Алгоритм Шеннона–Фано
    std::cout << "Задание 1: Алгоритм Шеннона–Фано" << std::endl;
    std::string data = "По-турецки говорили. Чяби, чяряби Чяряби, чяби - чяби. Мы набрали в рот воды.";
    std::vector<ShannonFanoNode> encodedSymbols = shannonFano(data);
    // Вывод закодированных символов и соответствующих кодов
    for (const auto& symbol : encodedSymbols) {
        std::cout << symbol.symbol << ": " << symbol.code << std::endl;
    }
	std::string message = "";
    for (char c : data) {
        for (const auto& symbol : encodedSymbols) {
            if (symbol.symbol.compare(std::string(1, c)) == 0) 
                message += symbol.code + " ";
        }
    }
    std::cout << "Закодированное сообщение: " << message << std::endl << std::endl;

    // Задание 2: Алгоритм Хафмана
    std::cout << "Задание 2: Алгоритм Хафмана" << std::endl;
    encode_haffman("Фамилия Имя Отчество");
    std::cout << std::endl << std::endl;

    // Задание 3: Алгоритм LZ77
    std::cout << "Задание 3: Алгоритм LZ77" << std::endl;
    data = "000101110110100111";
    int windowSize = 6;
    std::vector<LZ77Token> compressedData = LZ77Compress(data, windowSize);
    // Вывод сжатых данных
    for (const auto& token : compressedData) {
        std::cout << "(" << token.offset << ", " << token.length << " , " << token.nextChar << ") ";
    }
    std::cout << std::endl << std::endl;

    // Задание 4: Алгоритм LZ78
    std::cout << "Задание 4: Алгоритм LZ78" << std::endl;
    data = "менменаменаменатеп";
    std::vector<std::pair<int, char>> encodedData = LZ78Encode(data);
    // Вывод закодированных данных
    std::cout << "Закодированные данные: ";
    for (const auto& pair : encodedData) {
        std::cout << "(" << pair.first << ", " << pair.second << ") ";
    }
    std::cout << std::endl;
    // Раскодирование данных
    std::string decodedData = LZ78Decode(encodedData);
    std::cout << "Раскодированные данные: " << decodedData << std::endl;
    
    return 0;
}
