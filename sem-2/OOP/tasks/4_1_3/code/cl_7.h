#ifndef __CL_7__H
#define __CL_7__H
#include "cl_4.h"
#include "cl_5.h"
class cl_7 : public cl_4, public cl_5
{
private:
	string name;
public:
	cl_7(string name);
	string Get_Name();
};
#endif