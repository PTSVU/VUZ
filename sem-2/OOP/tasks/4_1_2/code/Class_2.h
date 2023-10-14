#ifndef __CLASS_2_H__
#define __CLASS_2_H__
#include "Class_1.h"

class Class_2 :public Class_1
{
public:
	Class_2(string name1, int num1);
	void Print();
private:
	string name;
	int num;
};
#endif