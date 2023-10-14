#ifndef __CL_3__H
#define __CL_3__H
#include "cl_1.h"
class cl_3 : public cl_1
{
private:
	string name;
public:
	cl_3(string name);
	string Get_Name();
};
#endif