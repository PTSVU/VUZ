#include "MyClass.h"
MyClass::MyClass(int i_data)
{
	open_num = i_data;
	hyden_num = i_data * 2;
}
void MyClass::Change()
{
	open_num = open_num + 1;
	hyden_num = hyden_num + 4;
}

void MyClass::HydenActive()
{
	HydenChange();
}
void MyClass::Print()
{
	cout << "Value of the available property " << open_num << "; Value of ahidden property " << hyden_num;
}
void MyClass::HydenChange()
{
	open_num = open_num + 5;
	hyden_num = hyden_num + 7;
}