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

void cl_base::print_tree(string delay)
{
	cout << endl << delay << get_name();
	for (auto p_sub : p_sub_objects)
	{
		p_sub->print_tree(delay + "    ");
	}
}

void cl_base::print_ready(string delay)
{
	cout << endl << delay;
	get_ready(get_name());
	for (auto p_sub : p_sub_objects)
	{
		p_sub->print_ready(delay + "    ");
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

int cl_base::count(string name)
{
	int count = 0;
	if (get_name() == name)
	{
		count++;
	}
	for (int i = 0; i < p_sub_objects.size(); i++)
	{
		count += p_sub_objects[i]->count(name);
	}
	return count;
}

cl_base* cl_base::search_by_name(string name)
{
	if (s_name == name)
	{
		return this;
	}
	cl_base* p_result = nullptr;
	for (int i = 0; i < p_sub_objects.size(); i++)
	{
		p_result = p_sub_objects[i]->search_by_name(name);
		if (p_result != nullptr)
		{
			return p_result;
		}
	}
	return nullptr;
}

cl_base* cl_base::search_cur(string name)
{
	if (count(name) != 1)
	{
		return nullptr;
	}
	return search_by_name(name);
}

cl_base* cl_base::search_from_root(string name)
{
	if (p_head_object != nullptr)
	{
		return p_head_object->search_from_root(name);
	}
	else
	{
		return search_cur(name);
	}
}

void cl_base::set_ready(int s_new_ready)
{
	if (s_new_ready != 0)
	{
		if (p_head_object == nullptr || p_head_object != nullptr && p_head_object->p_ready != 0)
		{
			p_ready = s_new_ready;
		}
	}
	else
	{
		p_ready = s_new_ready;
		for (int i = 0; i < p_sub_objects.size(); i++)
		{
			p_sub_objects[i]->set_ready(s_new_ready);
		}
	}
}

void cl_base::get_ready(string name)
{
	if (get_name() == name)
	{
		if (p_ready != 0)
		{
			cout << get_name() << " is ready";
		}
		else
		{
			cout << get_name() << " is not ready";
		}

	}
	else
	{
		for (int i = 0; i < p_sub_objects.size(); i++)
		{
			return p_sub_objects[i]->get_ready(name);
		}
	}
}