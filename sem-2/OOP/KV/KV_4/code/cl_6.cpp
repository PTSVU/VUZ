#include "cl_6.h"

cl_6::cl_6(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 6;
}

void cl_6::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 6)";
}

void cl_6::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}