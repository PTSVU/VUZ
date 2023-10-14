#ifndef __CL_SCREEN_H__
#define __CL_SCREEN_H__
#include "cl_base.h"

class cl_screen : public cl_base
{
public:
	cl_screen(cl_base* p_head_object, string s_name);
	void signal_f(string& msg);
	void handler_f(string msg);

	void handler_screen_from_all(string msg);
	void toBinary(unsigned int i);
};
#endif