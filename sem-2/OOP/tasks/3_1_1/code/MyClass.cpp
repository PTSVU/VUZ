#include "MyClass.h"
int dest = 1;
MyClass::MyClass(int l_mas)
{
	if (l_mas > 4)
	{
		p_mas = new int[l_mas];
		for (int i = 0; i < l_mas; i++)
		{
			p_mas[i] = l_mas;
		}
	}
	else
	{
		p_mas = nullptr;
		cout << l_mas << "?";
	}
}
MyClass::~MyClass()
{
	if ((p_mas != nullptr) && (dest == 1))
	{
		delete[] p_mas;
	}
	dest++;
}
void MyClass::Print(int l_mas)
{
	for (int i = 0; i < l_mas; i++)
	{
		cout << p_mas[i];
		if (i != l_mas - 1)
		{
			cout << " ";
		}
	}
}
void MyClass::Save(int s_mas[], int l_mas)
{
	for (int i = 0; i < l_mas; i++)
	{
		s_mas[i] = p_mas[i];
	}
}
void MyClass::Print_Saved(int s_mas[], int l_mas)
{
	for (int i = 0; i < l_mas; i++)
	{
		cout << s_mas[i];
		if (i != l_mas - 1)
		{
			cout << "  ";
		}
	}
}