#include "HashTable.h"

HashTable::HashTable() {
}

int HashTable::hashFunction(int key) const {
    return key % tableSize; // Простейшая функция хеширования: остаток от деления
}

bool HashTable::insert(int key, const Product& product) {
    rehash(tableSize + 1);
    int index = hashFunction(key);

    for (const auto& node : table[index]) {
        if (node.key == key) {
            cout << "Ключ уже существует. Вставка не удалась." << endl;
            return false;
        }
    }

    table[index].push_back({ key, product });
    return true;
}

bool HashTable::remove(int key) {
    int index = hashFunction(key);

    auto& list = table[index];
    for (auto it = list.begin(); it != list.end(); ++it) {
        if (it->key == key) {
            list.erase(it);
            rehash(tableSize - 1);
            return true;
        }
    }

    cout << "Ключ не найден. Удаление не удалось." << endl;
    return false;
}

list<Product> HashTable::find(int key) {
    int index = hashFunction(key);
    list<Product> result;

    for (const auto& node : table[index]) {
        if (node.key == key) {
            result.push_back(node.data);
        }
    }

    return result;
}

void HashTable::rehash(int newSize) {
    vector<list<HashNode>> newTable(newSize);

    for (const auto& list : table) {
        for (const auto& node : list) {
            int newIndex = node.key % newSize;
            newTable[newIndex].push_back(node);
        }
    }

    tableSize = newSize;
    table = move(newTable);
}
