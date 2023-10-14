#include "cl_calc.h"

cl_calc::cl_calc(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 2;
}

void cl_calc::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 2)";
}

void cl_calc::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}

void cl_calc::signal_calc_to_screen(string& msg)
{

}

void cl_calc::handler_calc_from_reader(string msg)
{
	if (msg == "+")
	{
		get_head()->i_result = get_head()->i_result + atoi((get_head()->s_operand_2).c_str());
	}
	else if (msg == "-")
	{
		get_head()->i_result = get_head()->i_result - atoi((get_head()->s_operand_2).c_str());
	}
	else if (msg == "*")
	{
		get_head()->i_result = get_head()->i_result * atoi((get_head()->s_operand_2).c_str());
	}
	else if (msg == "/")
	{
		if (atoi((get_head()->s_operand_2).c_str()) != 0)
		{
			get_head()->i_result = get_head()->i_result / atoi((get_head()->s_operand_2).c_str());
		}
		else
		{
			ostringstream ss;
			ss << setfill('0') << get_head()->i_result;
			get_head()->s_operand_2 = "     Division by zero";
			get_head()->i_result = 0;
		}
	}
	else if (msg == "%")
	{
		get_head()->i_result = get_head()->i_result % atoi((get_head()->s_operand_2).c_str());
	}

	emit_signal(SIGNAL_D(cl_calc::signal_calc_to_screen),
		to_string(get_head()->i_result));
}
