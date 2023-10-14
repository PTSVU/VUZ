#include "cl_cancel.h"

cl_cancel::cl_cancel(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 3;
}

void cl_cancel::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 3)";
}

void cl_cancel::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}

void cl_cancel::handler_cancel_from_reader(string msg)
{
	if (msg == "C")
	{
		get_head()->s_expression = "0";
		get_head()->s_operation = "";
		get_head()->s_operand_2 = "C";
		get_head()->i_result = 0;
	}
}
