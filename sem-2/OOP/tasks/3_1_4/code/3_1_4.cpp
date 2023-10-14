#include "MyClass.h"

MyClass func(int l)
{
	MyClass obj_func(l);
	return obj_func;
}

int main()
{
	int l;
	cin >> l;
	cout << l;
	if ((l > 2) && (l % 2 == 0))
	{
		MyClass obj_a;
		obj_a = func(l);
		obj_a.Input();
		obj_a.Met_b();
		MyClass obj_b(obj_a);
		obj_b.Met_a();
		obj_a.Print();
		cout << endl << obj_a.Summ();
		obj_b.Print();
		cout << endl << obj_b.Summ();
	}
	else
	{
		cout << "?";
	}
}