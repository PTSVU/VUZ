#ifndef __CLASS_4_H__
#define __CLASS_4_H__
#include "Class_3.h"

class Class_4 :public Class_3
{
public:
	Class_4(string name1, int num1);
	void Print();
private:
	string name;
	int num;
};
#endif