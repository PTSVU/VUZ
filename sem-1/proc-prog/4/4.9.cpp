#include < iostream >
using namespace std;

int main()
{
	setlocale(0, "");
	int a, b;
	cout << "введите исходный и результирующий разряды" << endl;
	cin >> a >> b;
	cout << "введите число" << endl;
	char chislo[124]{}; //хрананение задданного числа в виде символов
	char output[124]{}; //для вывода числа
	const char diapazone[25] = "0123456789ABCDEFGHIJKLMN"; //таблица соостветствия символов до 24 розряда
	cin >> chislo;
	cout << chislo << endl;
	int var10 = 0; //предстваление числа в 10-й системе
	int vara; //10-е значение символа
	int size = -1; //разрядность заданного числа

	for (auto el : chislo)
	{

		if (el == '\0') break;
		size++;
	}
	cout << size << endl;

	for (auto el : chislo) //перечеслитель заданного числа

	{
		vara = 0; //сброс текущего символа
		if (el == '\0') break;
		for (auto ch : diapazone)
		{

			if (el == ch) break; // сравнение найденного символа с таблицей, чтобы найти его порядковый номер, который и будет его значением.
			vara++; // если символ в этой итерации не найден, увеличить vara на 1
		}

		var10 += vara * pow(a, size--); //вычисление 10-чного числа
	}
	cout << var10 << endl;
	int indicate0 = var10;
	size = 0;

	do
	{
		indicate0 = var10 / b;
		vara = 0;

		for (auto ch : diapazone)
		{

			if (vara == (var10 - indicate0 * b))
			{
				output[size++] = ch;
				break;
			}
			vara++;
		}

		cout << var10 - indicate0 * b << endl;

		var10 = indicate0;

	} while (var10 > 0);

	size = 0;

	for (auto el : output) // вычисление размера строки результата для вывода
	{

		if (el == '\0') break;
		size++;
	}

	cout << "Результат: ";

	for (int i = 0; i < size; i++) //вывод знаков из строки в обратном порядке
	{
		cout << output[size - 1 - i];
	}
}