#include "Class_3.h"


Class_3::Class_3(string name1, int num1) :Class_2(name1, num1), name(name1 + "_3"), num(num1* num1* num1) {}

void Class_3::Print()
{
	cout << name + " " << num;
}