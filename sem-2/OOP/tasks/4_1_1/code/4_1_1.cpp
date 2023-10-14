#include "cl_child.h"

int main()
{
	int num_a, num_b;
	cin >> num_a >> num_b;
	cl_parent* obj_a = new cl_child(num_a, num_b);
	((cl_parent*)obj_a)->Print();
	cout << endl;
	((cl_child*)obj_a)->Print();
	if (num_a > 0)
	{
		((cl_child*)obj_a)->Pu_change(num_a + 1, num_b + 1);
		((cl_parent*)obj_a)->Pu_change(num_a - 1, num_b - 1);
		cout << endl;
		((cl_child*)obj_a)->Print();
		cout << endl;
		((cl_parent*)obj_a)->Print();
	}
	else
	{
		((cl_parent*)obj_a)->Pu_change(num_a + 1, num_b + 1);
		((cl_child*)obj_a)->Pu_change(num_a - 1, num_b - 1);
		cout << endl;
		((cl_parent*)obj_a)->Print();
		cout << endl;
		((cl_child*)obj_a)->Print();
	}
	delete obj_a;
}
