#include "cl_1.h"

cl_1::cl_1(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 1;
}

void cl_1::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 1)";
}

void cl_1::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}