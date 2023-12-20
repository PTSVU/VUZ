#include "Product.h"
using namespace std;


int main() {
    system("chcp 1251");
    Product a;
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
}