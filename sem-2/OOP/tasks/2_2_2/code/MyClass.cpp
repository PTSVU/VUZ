#include "MyClass.h"
MyClass::MyClass(int i_data)
{
	open_num = i_data;
	hyden_num = i_data * 3;
}
void MyClass::Change()
{
	open_num = open_num + 4;
	hyden_num = hyden_num + 1;
}
void MyClass::HydenActive()
{
	HydenChange();
}
void MyClass::Print()
{
	cout << "Value of the available property " << open_num << "; Value of a hidden property " << hyden_num;
}
void MyClass::HydenChange()
{
	open_num = open_num + 7;
	hyden_num = hyden_num + 5;
}