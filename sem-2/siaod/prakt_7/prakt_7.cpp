#include <iostream>
#include <list>
using namespace std;

int main()
{
	list <int> L1, L2, L;
	L1 = { 1, 3, 5, 7, 8, 9, 11 };
	L2 = { 2, 4, 6, 7, 8, 10, 11 };
	for (int n : L1)
	{
		L.push_back(n);
	}
	for (int n : L2)
	{
		L.push_back(n);
	}
	L.sort();
	L.unique();
	for (int n : L)
	{
		cout << n << " ";
	}
}