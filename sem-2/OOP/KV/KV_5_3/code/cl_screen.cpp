#include "cl_screen.h"

cl_screen::cl_screen(cl_base* p_head_object, string s_name) :cl_base(p_head_object, s_name)
{
	this->number = 5;
}

void cl_screen::signal_f(string& msg)
{
	cout << endl << "Signal from " << this->get_path();
	msg += " (class: 5)";
}

void cl_screen::handler_f(string msg)
{
	cout << endl << "Signal to " << get_path() << " Text:  " << msg;
}

void cl_screen::handler_screen_from_all(string msg)
{
	ostringstream ss;
	ss << setfill('0') << setw(4) << hex << uppercase << (unsigned short)get_head()->i_result;
	if (get_head()->s_operand_2 == "C" || get_head()->s_operand_2 == "Off")
	{
		get_head()->s_operand_2 = "";
	}
	else if (get_head()->i_result > 32767 || get_head()->i_result < -32768)
	{
		cout << endl << get_head()->s_expression << "     Overflow";
		get_head()->s_expression = "0";
	}
	else if (get_head()->s_operand_2 == "     Division by zero")
	{
		cout << endl << get_head()->s_expression << "     Division by zero";
		get_head()->s_expression = "0";
	}
	else if (get_head()->s_operand_2 != "     Division by zero")
	{
		if (f != 0)
		{
			cout << endl;
		}
		cout << get_head()->s_expression << "     HEX " << ss.str();
		cout << "  DEC " << get_head()->i_result;
		cout << "  BIN";
		toBinary(get_head()->i_result);
		f++;
	}
}

void cl_screen::toBinary(unsigned int i)
{
	bitset<16> binary(i);
	string binaryString = binary.to_string();
	for (int i = 12; i >= 0; i -= 4) {
		binaryString.insert(i, " ");
	}
	cout << binaryString;
}