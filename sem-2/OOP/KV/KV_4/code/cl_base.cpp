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
	get_root()->delete_links(this);
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
	return nullptr;
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

bool cl_base::change_head_obj(cl_base* new_head_obj)
{
	if (new_head_obj != nullptr)
	{
		cl_base* temp = new_head_obj;
		while (temp != nullptr)
		{
			temp = temp->p_head_object;
			if (temp == this)
			{
				return false;
			}
		}
		if (new_head_obj->get_sub_obj(get_name()) == nullptr && p_head_object != nullptr)
		{
			p_head_object->p_sub_objects.erase(find(p_head_object->p_sub_objects.begin(), p_head_object->p_sub_objects.end(), this));
			new_head_obj->p_sub_objects.push_back(this);
			p_head_object = new_head_obj;
			return true;
		}
	}
	return false;
}

void cl_base::delete_subordinate_obj(string name)
{
	cl_base* subordinate_obj = get_sub_obj(name);
	if (subordinate_obj != nullptr)
	{
		p_sub_objects.erase(find(p_sub_objects.begin(), p_sub_objects.end(), subordinate_obj));
		delete subordinate_obj;
	}
}

cl_base* cl_base::find_obj_by_coord(string s_object_path)
{
	if (s_object_path == "")
	{
		return nullptr;
	}
	cl_base* head_obj = this;
	string s_path_item;
	if (s_object_path == "." || s_object_path == "/")
	{
		return head_obj;
	}
	if (s_object_path[0] == '.')
	{
		s_object_path.erase(s_object_path.begin());
		return search_by_name(s_object_path);
	}
	if (s_object_path[1] == '/' && s_object_path[0] == '/')
	{
		s_object_path.erase(s_object_path.begin());
		s_object_path.erase(s_object_path.begin());
		return this->search_from_root(s_object_path);
	}
	if (s_object_path[0] == '/')
	{
		s_object_path.erase(s_object_path.begin());
		while (head_obj->p_head_object != nullptr)
		{
			head_obj = head_obj->p_head_object;
		}
	}
	stringstream ss_path(s_object_path);
	while (getline(ss_path, s_path_item, '/'))
	{
		head_obj = head_obj->get_sub_obj(s_path_item);
		if (head_obj == nullptr)
		{
			return nullptr;
		}
	}
	return head_obj;
}

void cl_base::print_from_current(int n)
{
	cout << endl;
	for (int i = 0; i < n; i++)
	{
		cout << "    ";
	}
	cout << s_name;
	for (auto p_subordinate_object : p_sub_objects)
	{
		p_subordinate_object->print_from_current(n + 1);
	}
}

void cl_base::set_connection(TYPE_SIGNAL p_signal, cl_base* p_target, TYPE_HANDLER p_handler)
{
	o_sh* p_value;
	for (int i = 0; i < connects.size(); i++)
	{
		if (connects[i]->p_signal == p_signal &&
			connects[i]->p_handler == p_handler &&
			connects[i]->p_target == p_target)
		{
			return;
		}
	}
	p_value = new o_sh();
	p_value->p_signal = p_signal;
	p_value->p_handler = p_handler;
	p_value->p_target = p_target;

	connects.push_back(p_value);
}

void cl_base::delete_connection(TYPE_SIGNAL p_signal, cl_base* p_target, TYPE_HANDLER p_handler)
{
	for (auto p_it = connects.begin(); p_it != connects.end(); p_it++)
	{
		if ((*p_it)->p_signal == p_signal &&
			(*p_it)->p_target == p_target &&
			(*p_it)->p_handler == p_handler)
		{
			delete* p_it;
			p_it = connects.erase(p_it);
			p_it--;
		}
	}
}

void cl_base::emit_signal(TYPE_SIGNAL p_signal, string s_massege)
{
	if (p_ready != 0)
	{
		TYPE_HANDLER pHandler;
		cl_base* pObject;
		(this->*p_signal)(s_massege);
		for (int i = 0; i < connects.size(); i++)
		{
			if (connects[i]->p_signal == p_signal)
			{
				pHandler = connects[i]->p_handler;
				pObject = connects[i]->p_target;
				if (pObject->p_ready != 0)
				{
					(pObject->*pHandler)(s_massege);
				}
			}
		}
	}
}
string cl_base::get_path()
{
	cl_base* p_head_object = this->get_head();
	if (p_head_object != nullptr)
	{
		if (p_head_object->get_head() == nullptr)
		{
			return p_head_object->get_path() + s_name;
		}
		else
		{
			return p_head_object->get_path() + "/" + s_name;
		}
	}
	return "/";
}

void cl_base::setState(int state)
{
	if (state == 0)
	{
		this->p_ready = 0;
		for (int i = 0; i < p_sub_objects.size(); i++) {
			p_sub_objects[i]->setState(0);
		}
		return;
	}
	if (this->p_head_object == nullptr || this->p_head_object->p_ready != 0) {
		this->p_ready = state;
	}
}



void cl_base::delete_links(cl_base* targ)
{
	for (auto p_it = connects.begin(); p_it != connects.end(); p_it++)
	{
		if ((*p_it)->p_target == targ)
		{
			delete (*p_it);
			connects.erase(p_it);
			p_it--;
		}
	}

	for (auto p_sub : p_sub_objects)
	{
		p_sub->delete_links(targ);
	}
}

cl_base* cl_base::get_root()
{
	if (p_head_object != nullptr)
	{
		p_head_object->get_root();
	}
	return this;
}
