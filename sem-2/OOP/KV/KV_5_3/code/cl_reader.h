#ifndef __CL_READER_H__
#define __CL_READER_H__
#include "cl_base.h"

class cl_reader : public cl_base
{
public:
	cl_reader(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);
	void handler_reader_from_app(string msg);
	void signal_reader_to_all(string& msg);
};
#endif