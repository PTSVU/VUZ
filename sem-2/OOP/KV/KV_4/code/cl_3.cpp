#include "cl_3.h"

cl_3::cl_3(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 3;
}

void cl_3::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 3)";
}

void cl_3::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}