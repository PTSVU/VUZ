#ifndef __CL_8__H
#define __CL_8__H
#include "cl_6.h"
#include "cl_7.h"
class cl_8 : public cl_6, public cl_7
{
private:
	string name;
public:
	cl_8(string name);
	string Get_Name();
};
#endif