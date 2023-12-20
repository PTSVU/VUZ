#ifndef __HASH_TABLE_H__
#define __HASH_TABLE_H__

#include "Product.h"
#include <list>

class HashTable {
private:
    struct HashNode {
        int key;
        Product data;
    };
    void rehash(int newSize);
public:
    HashTable();
    bool insert(int key, const Product& product);
    bool remove(int key);
    list<Product> find(int key);
    int tableSize = 0;
    vector<list<HashNode>> table;
    int hashFunction(int key) const;
};

#endif // !__HASH_TABLE_H__
