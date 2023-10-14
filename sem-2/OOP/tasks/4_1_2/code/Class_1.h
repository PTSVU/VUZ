#ifndef __CLASS_1_H__
#define __CLASS_1_H__
#include <iostream>
#include <string>
using namespace std;

class Class_1
{
public:
	Class_1(string name1, int num1);
	void Print();
private:
	string name;
	int num;
};
#endif