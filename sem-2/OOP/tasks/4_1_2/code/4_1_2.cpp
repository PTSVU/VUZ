#include "Class_4.h"

int main()
{
	int num;
	string name;
	cin >> name >> num;
	if (num >= 2 && num <= 10)
	{
		Class_1* obj = new Class_4(name, num);
		obj->Print();
		cout << endl;
		((Class_2*)obj)->Print();
		cout << endl;
		((Class_3*)obj)->Print();
		cout << endl;
		((Class_4*)obj)->Print();
		delete obj;
	}
}