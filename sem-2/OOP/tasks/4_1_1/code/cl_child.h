#ifndef __CL_CHILD_H__
#define __CL_CHILD_H__
#include "cl_parent.h"
class cl_child : public cl_parent
{
private:
	int pr_num;
public:
	int pu_num;
	cl_child(int num_a, int num_b);
	void Pu_change(int num_a, int num_b);
	void Print();
};
#endif