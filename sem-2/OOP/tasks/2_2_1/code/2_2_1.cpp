#include "MyClass.h"
int main()
{
	int i_data;
	cin >> i_data;
	MyClass obj(i_data);
	obj.Print();
	cout << endl;
	obj.Change();
	obj.Print();
	cout << endl;
	cin >> i_data;
	obj.open_num = obj.open_num * i_data;
	obj.Print();
	cout << endl;
	obj.HydenActive();
	obj.Print();
}