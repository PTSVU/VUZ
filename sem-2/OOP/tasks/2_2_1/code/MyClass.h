#ifndef __MYCLASS_H__
#define __MYCLASS_H__
#include <iostream>
using namespace std;
class MyClass
{
public:
	int open_num;
	MyClass(int i_data);
	void Change();
	void HydenActive();
	void Print();
private:
	int hyden_num;
	void HydenChange();
};
#endif