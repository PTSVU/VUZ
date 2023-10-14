#include "MyClass.h"
int main()
{
	int i_data;
	cin >> i_data;
	MyClass* p_obj = new MyClass(i_data);
	p_obj->Print();
	cout << endl;
	p_obj->Change();
	p_obj->Print();
	cout << endl;
	cin >> i_data;
	if (i_data > p_obj->open_num)
	{
		p_obj->open_num = i_data * 8;
	}
	p_obj->Print();
	cout << endl;
	p_obj->HydenActive();
	p_obj->Print();
	delete p_obj;
}