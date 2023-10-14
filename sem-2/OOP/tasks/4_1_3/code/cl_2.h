#ifndef __CL_2__H
#define __CL_2__H
#include "cl_1.h"
class cl_2 : public cl_1
{
private:
	string name;
public:
	cl_2(string name);
	string Get_Name();
};
#endif