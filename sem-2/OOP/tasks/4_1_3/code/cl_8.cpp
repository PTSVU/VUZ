#include "cl_8.h"
cl_8::cl_8(string s_name) :cl_6(s_name + "_8"), cl_7(s_name + "_8"), cl_1(s_name + "_8") //аврора ошибку не выдаёт
{
	name = s_name + "_8";
}
string cl_8::Get_Name()
{
	return name;
}