#include "cl_6.h"
cl_6::cl_6(string s_name) :cl_2(s_name + "_6"), cl_3(s_name + "_6")
{
	name = s_name + "_6";
}
string cl_6::Get_Name()
{
	return name;
}