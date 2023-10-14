#include <iostream>
using namespace std;
int main()
{
	double x, b, c;
	cout << "b= ";
	cin >> b;
	cout << "c= ";
	cin >> c;
	if (c != 0)
	{
		x = b/-c;
		if (x == -0)
		{
			x = 0;
			cout << "x= " << x;
		}
		else
		{
			cout << "x= " << x;
		}
	}
	else
	{
		cout << "nope";
	}
}