#include <iostream>

using namespace std;

int main()
{
	int n, h = 1, c = 1;
	double a, y, i1;
	cout << "enter integer number= ";
	cin >> n;
	cout << "enter no integer number= ";
	cin >> a;
	y = 1 / a;
	i1 = a * (a + 1);
	for (int i = 1; i < n; i++)
	{
		if (i > 1)
		{
			i1 = i1 * (a + i);
		}
		y = y + (i + 1) / i1;
	}
	cout << endl << "otvet= " << y;
}