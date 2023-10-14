#ifndef __CL_6__H
#define __CL_6__H
#include "cl_2.h"
#include "cl_3.h"
class cl_6 : public cl_2, public cl_3
{
private:
	string name;
public:
	cl_6(string name);
	string Get_Name();
};
#endif