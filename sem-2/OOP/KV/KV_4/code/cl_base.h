#ifndef __CL_BASE_H__
#define __CL_BASE_H__
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#define SIGNAL_D(signal_f) (TYPE_SIGNAL)(&signal_f)
#define HANDLER_D(handler_f) (TYPE_HANDLER)(&handler_f)
using namespace std;
class cl_base;

typedef void (cl_base::* TYPE_SIGNAL) (string& msg);
typedef void (cl_base::* TYPE_HANDLER) (string msg);

struct o_sh
{
	TYPE_SIGNAL p_signal;
	TYPE_HANDLER p_handler;
	cl_base* p_target;
};

class cl_base
{
private:
	string s_name;
	cl_base* p_head_object;
	vector <cl_base*> p_sub_objects;
	int p_ready = 1;
	vector<o_sh*> connects;
public:
	cl_base(cl_base* p_head_object, string s_name = "Base Object");
	bool set_name(string s_new_name);
	string get_name();
	cl_base* get_head();
	void print_tree(string delay = "");
	cl_base* get_sub_obj(string s_name);
	~cl_base();
	int count(string name);
	cl_base* search_by_name(string name);
	cl_base* search_cur(string name);
	cl_base* search_from_root(string name);
	void set_ready(int s_new_ready);
	void get_ready(string name);
	void print_ready(string delay = "");
	bool change_head_obj(cl_base* new_head_obj);
	void delete_subordinate_obj(string name);
	cl_base* find_obj_by_coord(string s_object_path);
	void print_from_current(int n = 0);
	void set_connection(TYPE_SIGNAL p_signal, cl_base* p_target, TYPE_HANDLER p_handler);
	void delete_connection(TYPE_SIGNAL p_signal, cl_base* p_target, TYPE_HANDLER p_handler);
	void emit_signal(TYPE_SIGNAL p_signal, string massege);
	string get_path();
	int number = 1;
	typedef void (cl_base::* TYPE_SIGNAL)(string&);
	typedef void (cl_base::* TYPE_HANDLER)(string);
	void setState(int state);
	void delete_links(cl_base* targ);
	cl_base* get_root();
};
#endif