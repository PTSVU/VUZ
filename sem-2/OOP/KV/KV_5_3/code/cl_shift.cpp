#include "cl_shift.h"

cl_shift::cl_shift(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 6;
}

void cl_shift::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 6)";
}

void cl_shift::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}

void cl_shift::handler_shift_from_reader(string msg)
{
	if (msg == "<<")
	{
		get_head()->i_result = get_head()->i_result << atoi((get_head()->s_operand_2).c_str());
	}
	else if (msg == ">>")
	{
		get_head()->i_result = get_head()->i_result >> atoi((get_head()->s_operand_2).c_str());
	}

	emit_signal(SIGNAL_D(cl_shift::signal_shift_to_screen),
		to_string(get_head()->i_result));
}

void cl_shift::signal_shift_to_screen(string& msg)
{

}