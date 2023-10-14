#include "Class_1.h"


Class_1::Class_1(string name1, int num1) :name(name1 + "_1"), num(num1) {}

void Class_1::Print()
{
	cout << name + " " << num;
}