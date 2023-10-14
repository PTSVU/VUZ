#include "cl_8.h"

int main()
{
	string name;
	cin >> name;
	cl_8* obj = new cl_8(name);
	cout << ((cl_1*)(cl_2*)(cl_6*)obj)->Get_Name() << endl;
	cout << ((cl_1*)(cl_3*)(cl_6*)obj)->Get_Name() << endl;
	cout << ((cl_1*)(cl_4*)(cl_7*)obj)->Get_Name() << endl;
	cout << ((cl_1*)(cl_5*)(cl_7*)obj)->Get_Name() << endl;
	cout << obj->cl_8::cl_6::cl_2::Get_Name() << endl;
	cout << obj->cl_8::cl_6::cl_3::Get_Name() << endl;
	cout << obj->cl_8::cl_7::cl_4::Get_Name() << endl;
	cout << obj->cl_8::cl_7::cl_5::Get_Name() << endl;
	cout << obj->cl_8::cl_6::Get_Name() << endl;
	cout << obj->cl_8::cl_7::Get_Name() << endl;
	cout << obj->Get_Name();
	delete obj;
}