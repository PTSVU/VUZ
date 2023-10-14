#ifndef __CL_5__H
#define __CL_5__H
#include "cl_1.h"
class cl_5 : public virtual cl_1
{
private:
	string name;
public:
	cl_5(string name);
	string Get_Name();
};
#endif