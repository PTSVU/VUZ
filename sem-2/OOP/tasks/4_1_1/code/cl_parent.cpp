#include "cl_parent.h"

cl_parent::cl_parent(int num_a, int num_b)
{
	Pr_change(num_a);
	pu_num = num_b;
}
void cl_parent::Pr_change(int par)
{
	pr_num = par * 2;
}
void cl_parent::Pu_change(int num_a, int num_b)
{
	Pr_change(num_a);
	pu_num = num_b;
}
void cl_parent::Print()
{
	cout << pr_num << "    " << pu_num;
}