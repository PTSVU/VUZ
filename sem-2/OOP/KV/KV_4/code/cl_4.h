#ifndef __CL_4_H__
#define __CL_4_H__
#include "cl_base.h"

class cl_4 : public cl_base
{
public:
	cl_4(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);
};
#endif