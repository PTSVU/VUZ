#include "Class_2.h"


Class_2::Class_2(string name1, int num1) :Class_1(name1, num1), name(name1 + "_2"), num(num1* num1) {}

void Class_2::Print()
{
	cout << name + " " << num;
}