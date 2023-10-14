#ifndef __CL_4__H
#define __CL_4__H
#include "cl_1.h"
class cl_4 : public virtual cl_1
{
private:
	string name;
public:
	cl_4(string name);
	string Get_Name();
};
#endif