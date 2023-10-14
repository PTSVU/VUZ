#include "MyClass.h"

MyClass* func(int l)
{
	MyClass* obj_func = new MyClass(l);
	obj_func->Mas_create();
	obj_func->Input();
	obj_func->Met_b();
	return obj_func;
}

int main()
{
	int l;
	cin >> l;
	cout << l;
	if ((l > 2) && (l % 2 == 0))
	{
		MyClass* obj_a;
		obj_a = func(l);
		obj_a->Met_a();
		MyClass* obj_b = new MyClass(obj_a);
		obj_b->Met_b();
		obj_a->Print();
		cout << endl << obj_a->Summ();
		obj_b->Print();
		cout << endl << obj_b->Summ();
		*obj_b = *obj_a;
		obj_a->Met_a();
		obj_b->Print();
		cout << endl << obj_b->Summ();
		delete obj_a;
		delete obj_b;
	}
	else
	{
		cout << "?";
	}
}