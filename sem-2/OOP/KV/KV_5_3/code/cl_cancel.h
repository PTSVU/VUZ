#ifndef __CL_CANCEL_H__
#define __CL_CANCEL_H__
#include "cl_base.h"

class cl_cancel : public cl_base
{
public:
	cl_cancel(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);

	void handler_cancel_from_reader(string msg);
};
#endif