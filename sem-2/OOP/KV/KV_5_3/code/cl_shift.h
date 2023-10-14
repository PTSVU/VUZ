#ifndef __CL_SHIFT_H__
#define __CL_SHIFT_H__
#include "cl_base.h"

class cl_shift : public cl_base
{
public:
	cl_shift(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);

	void handler_shift_from_reader(string msg);
	void signal_shift_to_screen(string& msg);
};
#endif