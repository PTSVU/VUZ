#include "FileWithHashTable.h"

FileWithHashTable::FileWithHashTable() {
    binaryFilename = file.fileName;
    int key;
    cout << "������� ����: ";
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
        cout << "\n��������:"
            << "\n\t0 - ��������� �����"
            << "\n\t1 - �������� ����� ������"
            << "\n\t2 - ��������� .txt � .bin(�������� ����)"
            << "\n\t3 - ����� ����������� .txt"
            << "\n\t4 - ����� ����������� .bin"
            << "\n\t5 - ���������� ������ ��������� �����"
            << "\n\t6 - ��������� ������ �� ������"
            << "\n\t7 - �������� �� ������"
            << "\n\t8 - �������� ����� � ��������� ����������� ������" << endl;
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
            cout << "\n���������� � �������� ����." << endl;
            break;
        case 3:
            a.print_txt();
            break;
        case 4:
            a.print_bin();
            break;
        case 5:
            cout << "������� �������� ����� ��� ����������: ";
            cin >> saveName;
            a.bin_to_txt(saveName);
            cout << "\n���������� � ��������� ����." << endl;
            break;
        case 6:
            int var;
            cout << "\n���������� ��� ����� ID ����� ��������:\n";
            a.print_txt();
            cout << endl;
            cin >> var;
            a.change_inf(var);
            break;
        case 7:
            int ch;
            cout << "������� ����� ��� ��������: ";
            cin >> ch;
            a.DelCh(ch);
            break;
        case 8:
            a.country_to_txt();
            cout << "\n���� ������\n";
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
