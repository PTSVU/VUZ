#include "cl_2.h"

cl_2::cl_2(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 2;
}

void cl_2::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 2)";
}

void cl_2::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}