#include "cl_4.h"
cl_4::cl_4(string s_name) :cl_1(s_name + "_4")
{
	name = s_name + "_4";
}
string cl_4::Get_Name()
{
	return name;
}