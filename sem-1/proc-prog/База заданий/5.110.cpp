#include <iostream>
#include <fstream>

using namespace std;
int getIntNumber();
void ismonk(int number);
int generalteacher(int teacher1, int teacher2);
int  teachers[600] = { 0 }, students[600][3] = { 0 };

int main() {
	int i, task, monk, first, second, third;

	setlocale(LC_ALL, "Russian");
	/*cout << "Задание «Монахи»\n\n";*/
	cout << "  Задача 1) по номеру монаха узнать, был ли такой монах и если был, то кто были его учитель, учитель его учителя и т.д. до самого Святого Павла;\n";
	cout << "  Задача 2) по двум монашеским номерам найти их общего ближайшего учителя.\n\n";
	ifstream in;
	in.open("5.110.txt", ios::in);
	for (i = 0; i < 6; i++)
	{
		in >> monk >> first >> second >> third;
		students[monk][0] = first;
		students[monk][1] = second;
		students[monk][2] = third;
		teachers[first] = monk;
		teachers[second] = monk;
		teachers[third] = monk;
	}
	in.close();

	cout << "Введите номер задачи:  ";
	task = getIntNumber();
	switch (task)
	{
	case 1:
		cout << "\nВведите номер монаха:  ";
		monk = getIntNumber();
		if (teachers[monk] == 0)
		{
			cout << monk << " не монах";
		}
		else
		{
			cout << monk << " монах, его учителя ";
			ismonk(monk);
		}
		cout << endl;
		break;
	case 2:
		cout << "\nВведите номера двух монахов через пробел:  ";
		cin >> first;
		cin >> second;
		if (teachers[first] == 0)
		{
			cout << first << " не монах" << endl << endl;
		}

		else
		{
			if (teachers[second] == 0)
			{
				cout << second << " не монах" << endl << endl;
			}
			else
			{
				cout << first << " и " << second << " оба монахи и их общий учитель ";
				first = teachers[first];
				second = teachers[second];
				cout << generalteacher(first, second) << endl << endl;
			}
		}
		break;
	default:
		cout << endl << task << " неверный номер задачи\n\n";
		break;
	}

	system("pause");
	return 1;
}

void ismonk(int number)
{
	if (teachers[number] == 1)
	{
		return;
	}
	else
	{
		cout << teachers[number] << " ";
		ismonk(teachers[number]);
	}
}

int generalteacher(int teacher1, int teacher2)
{
	if (teacher1 == teacher2)
		return (teacher1);
	else
	{
		if (teacher1 > teacher2)
		{
			teacher1 = teachers[teacher1];
		}
		else
		{
			teacher2 = teachers[teacher2];
		}
		generalteacher(teacher1, teacher2);
	}
}

int getIntNumber()
{
	int number;
	cin >> number;
	while (number < 0)
	{
		cout << endl; "Число не может быть негативным ";
		cin >> number;
	}
	return number;
}