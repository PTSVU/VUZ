#ifndef __CL_6_H__
#define __CL_6_H__
#include "cl_base.h"

class cl_6 : public cl_base
{
public:
	cl_6(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);
};
#endif