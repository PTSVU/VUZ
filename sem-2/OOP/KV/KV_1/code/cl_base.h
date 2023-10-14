#ifndef __CL_BASE_H__
#define __CL_BASE_H__
#include <iostream>
#include <string>
#include <vector>
using namespace std;


class cl_base
{
private:
	string s_name;
	cl_base* p_head_object;
	vector <cl_base*> p_sub_objects;
public:
	cl_base(cl_base* p_head_object, string s_name = "Base Object");
	bool set_name(string s_new_name);
	string get_name();
	cl_base* get_head();
	void print_tree();
	cl_base* get_sub_obj(string s_name);
	~cl_base();
};
#endif