#include "cl_reader.h"

cl_reader::cl_reader(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 4;
}

void cl_reader::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 4)";
}

void cl_reader::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}

void cl_reader::handler_reader_from_app(string msg)
{
	string s_cmd;
	cin >> s_cmd;
	if (s_cmd == "C" || s_cmd == "Off")
	{
		emit_signal(SIGNAL_D(cl_reader::signal_reader_to_all), s_cmd);
	}
	else if (s_cmd == "+" || s_cmd == "-" || s_cmd == "*" || s_cmd == "/" || s_cmd == "%" || s_cmd == "<<" || s_cmd == ">>")
	{
		get_head()->s_operation = s_cmd;
		get_head()->s_expression += (" " + s_cmd);

		cin >> get_head()->s_operand_2;
		get_head()->s_expression += (" " + get_head()->s_operand_2);
		emit_signal(SIGNAL_D(cl_reader::signal_reader_to_all), s_cmd);

	}
	else
	{
		get_head()->s_expression = s_cmd;
		get_head()->i_result = atoi((get_head()->s_expression).c_str());
	}
}

void cl_reader::signal_reader_to_all(string& msg)
{

}