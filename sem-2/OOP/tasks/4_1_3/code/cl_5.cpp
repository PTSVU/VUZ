#include "cl_5.h"
cl_5::cl_5(string s_name) :cl_1(s_name + "_5")
{
	name = s_name + "_5";
}
string cl_5::Get_Name()
{
	return name;
}