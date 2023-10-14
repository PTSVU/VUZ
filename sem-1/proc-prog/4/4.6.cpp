#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ofstream t("4.6.txt");
	string a;
	cout << "enter rim num= ";
	getline(cin, a);
	t << a;
	t.close();
	char b[100000];
	ifstream f("4.6.txt");
	f.getline(b, 100000);
	f.close();
	int l, r = 0;
	l = sizeof(b);
	for (int i = 0; i < l; i++)
	{
		if (b[i] == 73 or b[i] == 105)
		{
			if (b[i+1] == 86 or b[i+1] == 118)
			{
				r = r + 4;
				i = i + 1;
			}
			else if (b[i+1] == 88 or b[i+1] == 120)
			{
				r = r + 9;
				i = i + 1;
			}
			else
			{
				r = r + 1;
			}
		}
		else if (b[i] == 86 or b[i] == 118)
		{
			r = r + 5;
		}
		else if (b[i] == 88 or b[i] == 120)
		{
			if (b[i+1] == 76 or b[i+1] == 108)
			{
				r = r + 40;
				i = i + 1;
			}
			else if (b[i+1] == 67 or b[i+1] == 99)
			{
				r = r + 90;
				i = i + 1;
			}
			else
			{
				r = r + 10;
			}
		}
		else if (b[i] == 76 or b[i] == 108)
		{
			r = r + 50;
		}
		else if (b[i] == 67 or b[i] == 99)
		{
			if (b[i+1] == 68 or b[i+1] == 100)
			{
				r = r + 400;
				i = i + 1;
			}
			else if (b[i+1] == 77 or b[i+1] == 109)
			{
				r = r + 900;
				i = i + 1;
			}
			else
			{
				r = r + 100;
			}
		}
		else if (b[i] == 68 or b[i] == 100)
		{
			r = r + 500;
		}
		else if (b[i] == 77 or b[i] == 109)
		{
			r = r + 1000;
		}
	}
	cout << "rim num= " << r << endl << endl;
}