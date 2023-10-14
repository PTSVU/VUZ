#ifndef __CL_PARENT_H__
#define __CL_PARENT_H__
#include <iostream>
using namespace std;
class cl_parent
{
private:
	int pr_num;
	void Pr_change(int par);
public:
	int pu_num;
	cl_parent(int num_a, int num_b);
	void Pu_change(int num_a, int num_b);
	void Print();
};
#endif