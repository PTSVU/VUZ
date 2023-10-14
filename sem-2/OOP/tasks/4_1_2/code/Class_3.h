#ifndef __CLASS_3_H__
#define __CLASS_3_H__
#include "Class_2.h"

class Class_3 :public Class_2
{
public:
	Class_3(string name1, int num1);
	void Print();
private:
	string name;
	int num;
};
#endif