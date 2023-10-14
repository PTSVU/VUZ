#ifndef __CL_CALC_H__
#define __CL_CALC_H__
#include "cl_base.h"

class cl_calc : public cl_base
{
public:
	cl_calc(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);

	void signal_calc_to_screen(string& msg);
	void handler_calc_from_reader(string msg);
};
#endif