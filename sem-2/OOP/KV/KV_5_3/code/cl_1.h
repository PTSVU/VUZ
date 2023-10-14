#ifndef __CL_1_H__
#define __CL_1_H__
#include "cl_base.h"

class cl_1 : public cl_base
{
public:
	cl_1(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);
};
#endif