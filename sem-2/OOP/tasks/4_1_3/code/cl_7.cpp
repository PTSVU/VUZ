#include "cl_7.h"
cl_7::cl_7(string s_name) :cl_4(s_name + "_7"), cl_5(s_name + "_7"), cl_1(s_name + "_1")
{
	name = s_name + "_7";
}
string cl_7::Get_Name()
{
	return name;
}