#include "cl_2.h"
cl_2::cl_2(string s_name) :cl_1(s_name + "_2")
{
	name = s_name + "_2";
}
string cl_2::Get_Name()
{
	return name;
}