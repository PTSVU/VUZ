#ifndef __MYCLASS_H__
#define __MYCLASS_H__
#include <iostream>
using namespace std;
class MyClass
{
public:
	MyClass();
	MyClass(int l);
	MyClass(MyClass& obj);
	~MyClass();
	void Input();
	void Met_a();
	void Met_b();
	int Summ();
	void Print();
private:
	int* mas = nullptr, len = 0;
};
#endif