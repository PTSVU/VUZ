#include <iostream>
#include <cmath>
#include <math.h>
#include <stack>
using namespace std;

int main()
{
	int n;
	int m;
	int k = 0;
	int flag = 0;
	int max = 0;
	int f = 0;
	int v[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	int k0 = 0;
	int k1 = 0;

	cout << "vagon number= ";
	cin >> n; 
	cout << endl;

	for (int i = 0; i < n; i++)
	{
		cin >> m;
		if (m >= 1 && m <= 4 || m == 53 || m == 54) {
			v[0] += 1;
		}
		if (m >= 5 && m <= 8 || m == 51 || m == 52) {
			k1++;
			v[1] += 1;
		}
		if (m >= 9 && m <= 12 || m == 49 || m == 50) {
			v[2] += 1;
		}
		if (m >= 13 && m <= 16 || m == 47 || m == 48) {
			v[3] += 1;
		}
		if (m >= 17 && m <= 20 || m == 45 || m == 46) {
			v[4] += 1;
		}
		if (m >= 21 && m <= 24 || m == 43 || m == 44) {
			v[5] += 1;
		}
		if (m >= 25 && m <= 28 || m == 41 || m == 42) {
			v[6] += 1;
		}
		if (m >= 29 && m <= 32 || m == 39 || m == 40) {
			v[7] += 1;
		}
		if (m >= 33 && m <= 36 || m == 37 || m == 38) {
			v[8] += 1;
		}
	}
	for (int i = 0; i < 9; i++) {
		if (v[i] == 6) {
			f++;
		}
		if (f > max) {
			max = f;
		}
		else {
			f = max;
		}
	}
	cout <<  f << endl;
}