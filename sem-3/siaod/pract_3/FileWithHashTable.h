#ifndef __FILE_WITH_HASH_TABLE_H__
#define __FILE_WITH_HASH_TABLE_H__

#include "Product.h"
#include "HashTable.h"
#include <list>


class FileWithHashTable {
public:
    FileWithHashTable();
    void loadFromFile(int key);
    bool insert(int key);
    bool remove(int key);
    list <Product> find(int key);
    void print();
    Product BinCLI(Product a);
    void change(int key);

private:
    Product file;
    string binaryFilename;
    HashTable hashTable;
};

#endif // !__FILE_WITH_HASH_TABLE_H__
