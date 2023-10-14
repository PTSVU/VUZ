#include "cl_application.h"

cl_application::cl_application(cl_base* p_head_object) :cl_base(p_head_object) {}

void cl_application::build_tree_objects()
{
	string s_head, s_sub;
	int s_num_obj, s_redy_obj;
	cl_base* p_head = this, * p_sub = nullptr;
	cin >> s_head;
	set_name(s_head);
	cout << set_name(s_head);
	while (true)
	{
		cin >> s_head;
		if (s_head == "endtree")
		{
			break;
		}
		cin >> s_sub >> s_num_obj;
		if (p_head != nullptr)
		{
			p_head = find_obj_by_coord(s_head);
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
		else
		{
			cout << "Object tree";
			print_from_current();
			cout << endl << "The head object " << s_head << " is not found";
			exit(1);
		}
	}
}

void cl_application::build_commands()
{
	string command;
	string object_name;
	cl_base* current_obj = this;
	while (command != "END")
	{
		cin >> command;
		cin >> object_name;
		cl_base* temp = current_obj->find_obj_by_coord(object_name);
		if (command == "SET")
		{
			if (temp != nullptr)
			{
				current_obj = temp;
				cout << "Object is set: " << current_obj->get_name() << endl;
			}
			else
			{
				cout << "The object was not found at specified coordinate: " << object_name << endl;
			}
		}
		if (command == "FIND")
		{
			if (temp != nullptr && temp->search_by_name(object_name) == nullptr)
			{
				cout << object_name << "     Object name: " << temp->get_name() << endl;
			}
			else
			{
				cout << object_name << "     Object is not found" << endl;
			}
		}
		if (command == "MOVE")
		{
			if (temp != nullptr)
			{
				if (current_obj->change_head_obj(temp))
				{
					cout << "New head object: " << temp->get_name() << endl;
				}
				else if (temp->get_sub_obj(current_obj->get_name()))
				{
					cout << object_name << "     Dubbing the names of subordinate objects" << endl;
				}
				else
				{
					cout << object_name << "     Redefining the head object failed" << endl;
				}
			}
			else
			{
				cout << object_name << "     Head object is not found" << endl;
			}
		}
		if (command == "DELETE")
		{
			if (current_obj->search_by_name(object_name) != nullptr
				&& current_obj->get_name() != object_name)
			{
				vector <cl_base*> path;
				cl_base* temp2 = current_obj;
				while (temp2->get_head() != nullptr)
				{
					path.insert(path.begin(), temp2);
					temp2 = temp2->get_head();
				}
				path.insert(path.end(), current_obj->search_by_name(object_name));
				cout << "The object ";
				for (auto path_item : path)
				{
					cout << "/" << path_item->get_name();
				}
				cout << " has been deleted" << endl;
				current_obj->delete_subordinate_obj(object_name);
			}
		}
	}
}

int cl_application::exec_app()
{
	cout << "Object tree";
	print_from_current();
	cout << endl;
	build_commands();
	cout << "Current object hierarchy tree";
	print_from_current();
	return 0;
}