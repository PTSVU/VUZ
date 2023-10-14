#include "MyClass.h"

void func(MyClass& obj)
{
	MyClass obj_func(obj);
	obj_func.Met_b();
	cout << endl << obj_func.Summ();
}

int main()
{
	int l;
	cin >> l;
	cout << l;
	if ((l > 2) && (l % 2 == 0))
	{
		MyClass obj_a(l);
		obj_a.Input();
		func(obj_a);
		obj_a.Met_a();
		cout << endl << obj_a.Summ();
	}
	else
	{
		cout << "?";
	}
}