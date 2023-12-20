#include "FileWithHashTable.h"


int main() {
	system("chcp 1251");
	int var = 1;
	FileWithHashTable file;
	while (var > 0) {
        cout << "1: Добавить элемент" << endl;
		cout << "2: Изменить элемент" << endl;
		cout << "3: Удалить элемент" << endl;
		cout << "4: Найти элемент" << endl;
		cout << "5: Вывести хеш-таблицу" << endl;
		cin >> var;
		switch (var)
		{
            case 1: {
					int key;
					cout << "Введите ключ: ";
					cin >> key;
					file.insert(key);
					break;
            }
			case 2: {
					int key;
					cout << "Введите ключ: ";
					cin >> key;
					file.change(key);
					break;
			}
			case 3: {
					int key;
					cout << "Введите ключ: ";
					cin >> key;
					file.remove(key);
					break;
			}
			case 4: {
					int key;
					cout << "Введите ключ: ";
					cin >> key;
					for (auto prod : file.find(key)) {
						prod.print_txt();
					}
					break;
			}
			case 5: {
					file.print();
					break;
			}
			default: {
					break;
			}
		}
	}
}