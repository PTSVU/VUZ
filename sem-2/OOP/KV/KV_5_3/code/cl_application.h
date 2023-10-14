#ifndef __CL_APPLICATION_H__
#define __CL_APPLICATION_H__
#include "cl_base.h"
#include "cl_1.h"
#include "cl_calc.h"
#include "cl_cancel.h"
#include "cl_reader.h"
#include "cl_screen.h"
#include "cl_shift.h"
class cl_application : public cl_base
{
public:
	cl_application(cl_base* p_head_object);
	void build_tree_objects();
	int exec_app();
	void build_commands();
	void setConnections();
	void signal_app_to_reader(string& msg);
	void handler_app_from_reader(string msg);
};
#endif