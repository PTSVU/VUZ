#include "cl_application.h"

cl_application::cl_application(cl_base* p_head_object) :cl_base(p_head_object) {}

void cl_application::build_tree_objects()
{
	string s_head, s_sub;
	int s_num_obj, s_redy_obj;
	cl_base* p_head = this, * p_sub = nullptr;
	cin >> s_head;
	set_name(s_head);
	while (true)
	{
		cin >> s_head;
		if (s_head == "endtree")
		{
			break;
		}
		cin >> s_sub >> s_num_obj;
		if (search_from_root(s_head) != nullptr && search_from_root(s_head)->count(s_sub) <= 1)
		{
			p_head = search_from_root(s_head);
			switch (s_num_obj)
			{
			case 1:
				p_sub = new cl_1(p_head, s_sub);
				break;
			case 2:
				p_sub = new cl_2(p_head, s_sub);
				break;
			case 3:
				p_sub = new cl_3(p_head, s_sub);
				break;
			case 4:
				p_sub = new cl_4(p_head, s_sub);
				break;
			case 5:
				p_sub = new cl_5(p_head, s_sub);
				break;
			case 6:
				p_sub = new cl_6(p_head, s_sub);
				break;
			}
		}
	}
	while (cin >> s_head >> s_redy_obj)
	{
		search_from_root(s_head)->set_ready(s_redy_obj);
	}
}

int cl_application::exec_app()
{
	cout << "Object tree";
	print_tree();
	cout << endl << "The tree of objects and their readiness";
	print_ready();
	return 0;
}