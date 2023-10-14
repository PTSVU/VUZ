#include "cl_3.h"
cl_3::cl_3(string s_name) :cl_1(s_name + "_3")
{
	name = s_name + "_3";
}
string cl_3::Get_Name()
{
	return name;
}