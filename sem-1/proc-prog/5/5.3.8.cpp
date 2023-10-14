#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	ofstream t("5.3.txt");
	string a;
	getline(cin, a);
	t << a;
	t.close();
	char b[100];
	ifstream f("5.3.txt");
	f.getline(b, 100);
	f.close();
	cout << endl << "file= " << b << endl;
	int l;
	l = sizeof(b);
	cout << "text in ASCII= ";
	for (int i = 0; i < l; i++)
	{
		if (b[i] == 32)
		{
			cout << " ";
		}
		else if (b[i] == -52)
		{
			cout << "";
		}
		else
		{
			if (b[i] == 0)
			{
				"";
			}
			else
			{
				cout << int(b[i]) << " ";
			}
		}
	}
}