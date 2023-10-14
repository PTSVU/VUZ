#include "MyClass.h"
int main()
{
	int l_mas_a, l_mas_b, * s_mas;
	cin >> l_mas_a;
	MyClass obj_a(l_mas_a);
	if (obj_a.p_mas != nullptr)
	{
		cin >> l_mas_b;
		MyClass obj_b(l_mas_b);
		if (obj_b.p_mas != nullptr)
		{
			s_mas = new int[l_mas_a];
			obj_a.Save(s_mas, l_mas_a);
			obj_a = obj_b;
			obj_a.Print_Saved(s_mas, l_mas_a);
			cout << endl;
			obj_b.Print(l_mas_b);
			delete[] s_mas;
		}
	}
}