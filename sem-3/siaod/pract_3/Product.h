#ifndef __PRODUCT_H__
#define __PRODUCT_H__
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

class Product {
public:
    Product();
    string fileName = "baseName";
    void print_bin();
    void print_txt();
    void bin_to_txt(string saveName);
    void txt_to_bin();
    void PrintCh(int num);
    void DelCh(int num);
    void ProductAdd();
    void country_to_txt();
    void change_inf(int var);

    // Поля для записи в файл
    vector <int> id = { 0 };
    vector <string> name = { "Product name" };
    vector <string> code = { "000000" };
    vector <string> manufacturer = { "Manufacturer name" };
    vector <double> price = { 0.00 };
    vector <string> country = { "Country" };

private:

    void TxtSave(int num);
    bool fileExists(const string& filename);
    string space_del(const string& str);
    void vector_reconstruction();
};
#endif