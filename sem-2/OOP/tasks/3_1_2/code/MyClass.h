#ifndef __MYCLASS_H__
#define __MYCLASS_H__
#include <iostream>
using namespace std;
class MyClass
{
public:
	MyClass(int l_mas);
	void Print(int l_mas);
	void Save(int s_mas[], int l_mas);
	void Print_Saved(int s_mas[], int l_mas);
	~MyClass();
private:
	int* p_mas;
};
#endif