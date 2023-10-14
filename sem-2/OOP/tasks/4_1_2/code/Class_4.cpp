#include "Class_4.h"


Class_4::Class_4(string name1, int num1) :Class_3(name1, num1), name(name1 + "_4"), num(num1* num1* num1* num1) {}

void Class_4::Print()
{
	cout << name + " " << num;
}