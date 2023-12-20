#include "FileWithHashTable.h"

FileWithHashTable::FileWithHashTable() {
    binaryFilename = file.fileName;
    int key;
    cout << "Введите ключ: ";
    cin >> key;
	loadFromFile(key);
}

void FileWithHashTable::loadFromFile(int key) {
	hashTable.insert(key, file);
}

bool FileWithHashTable::insert(int key) {
    Product a;
    return hashTable.insert(key, BinCLI(a));
}

bool FileWithHashTable::remove(int key) {
    return hashTable.remove(key);
}

list<Product> FileWithHashTable::find(int key) {
    return hashTable.find(key);
}

void FileWithHashTable::print()
{
	for (auto lis : hashTable.table) {
        for (auto prod : lis) {
            prod.data.print_txt();
            cout << "-----------------" << endl;
        }
	}
}

Product FileWithHashTable::BinCLI(Product a) {
    int swc;
    bool wh = true;
    string saveName;
    while (wh)
    {
        cout << "\nДействия:"
            << "\n\t0 - Остановка ввода"
            << "\n\t1 - Добавить новые данные"
            << "\n\t2 - перевести .txt в .bin(двоичный файл)"
            << "\n\t3 - вывод содержимого .txt"
            << "\n\t4 - вывод содержимого .bin"
            << "\n\t5 - сохранение данных двоичного файла"
            << "\n\t6 - изменения данных по номеру"
            << "\n\t7 - удаление по номеру"
            << "\n\t8 - создание файла о поставках определённой страны" << endl;
        cin >> swc;
        switch (swc)
        {
        case 0:
            wh = false;
            break;
        case 1:
            a.ProductAdd();
            break;
        case 2:
            a.txt_to_bin();
            cout << "\nПереведено в двоичный файл." << endl;
            break;
        case 3:
            a.print_txt();
            break;
        case 4:
            a.print_bin();
            break;
        case 5:
            cout << "Введите название файла для сохранения: ";
            cin >> saveName;
            a.bin_to_txt(saveName);
            cout << "\nПереведено в текстовый файл." << endl;
            break;
        case 6:
            int var;
            cout << "\nИнформацию под каким ID нужно изменить:\n";
            a.print_txt();
            cout << endl;
            cin >> var;
            a.change_inf(var);
            break;
        case 7:
            int ch;
            cout << "Введите номер для удаления: ";
            cin >> ch;
            a.DelCh(ch);
            break;
        case 8:
            a.country_to_txt();
            cout << "\nФайл создан\n";
            break;
        default:
            wh = false;
            break;
        }
    }
    return a;
}

void FileWithHashTable::change(int key)
{
    Product prod = hashTable.table[hashTable.hashFunction(key)].front().data;
    BinCLI(prod);
}
