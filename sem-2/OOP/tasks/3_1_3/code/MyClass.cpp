#include "MyClass.h"


MyClass::MyClass()
{
	cout << "\nDefault constructor";
}

MyClass::MyClass(int l)
{
	cout << "\nConstructor set";
	len = l;
	mas = new int[len];
}

MyClass::~MyClass()
{
	cout << "\nDestructor";
	if (mas != nullptr)
	{
		delete[]mas;
	}
}

MyClass::MyClass(MyClass& obj)
{
	cout << "\nCopy constructor";
	len = obj.len;
	mas = new int[len];
	for (int i = 0; i < len; i++)
	{
		mas[i] = obj.mas[i];
	}
}

void MyClass::Input()
{
	for (int i = 0; i < len; i++)
	{
		cin >> mas[i];
	}
}

void MyClass::Met_a()
{
	for (int i = 0; i + 1 < len; i = i + 2)
	{
		mas[i] = mas[i] + mas[i + 1];
	}
}

void MyClass::Met_b()
{
	for (int i = 0; i + 1 < len; i = i + 2)
	{
		mas[i] = mas[i] * mas[i + 1];
	}
}

int MyClass::Summ()
{
	int summ = 0;
	for (int i = 0; i < len; i++)
	{
		summ = summ + mas[i];
	}
	return summ;
}