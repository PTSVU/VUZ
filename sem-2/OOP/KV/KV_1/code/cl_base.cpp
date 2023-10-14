#include "cl_base.h"

cl_base::cl_base(cl_base* p_head_object, string s_name)
{
	this->s_name = s_name;
	this->p_head_object = p_head_object;
	if (p_head_object != nullptr)
	{
		p_head_object->p_sub_objects.push_back(this);
	}
}

cl_base::~cl_base()
{
	for (int i = 0; i < p_sub_objects.size(); i++)
	{
		delete p_sub_objects[i];
	}
}

bool cl_base::set_name(string s_new_name)
{
	if (get_head() != nullptr)
	{
		for (int i = 0; i < get_head()->p_sub_objects.size(); i++)
		{
			if (get_head()->p_sub_objects[i]->get_name() == s_new_name)
			{
				return false;
			}
		}
	}
	s_name = s_new_name;
	return true;
}

void cl_base::print_tree()
{
	if (p_sub_objects.size() == 0)
	{
		return;
	}
	else
	{
		cout << endl << get_name();
		for (int i = 0; i < p_sub_objects.size(); i++)
		{
			cout << "  " << p_sub_objects[i]->get_name();
		}
		for (int i = 0; i < p_sub_objects.size(); i++)
		{
			p_sub_objects[i]->print_tree();
		}
	}
}

string cl_base::get_name()
{
	return s_name;
}

cl_base* cl_base::get_head()
{
	return p_head_object;
}

cl_base* cl_base::get_sub_obj(string s_name)
{
	for (int i = 0; i < p_sub_objects.size(); i++)
	{
		if (p_sub_objects[i]->s_name == s_name)
		{
			return p_sub_objects[i];
		}
	}
	return 0;
}