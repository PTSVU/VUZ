#include "cl_child.h"

cl_child::cl_child(int num_a, int num_b) :cl_parent(num_a, num_b)
{
	pr_num = num_a;
	pu_num = num_b;
}
void cl_child::Pu_change(int num_a, int num_b)
{
	pr_num = num_a;
	pu_num = num_b;
}
void cl_child::Print()
{
	cout << pr_num << "    " << pu_num;
}