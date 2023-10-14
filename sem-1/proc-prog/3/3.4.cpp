#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	ofstream t("t3.4.txt");
	string a;
	getline(cin, a);
	t << a;
	t.close();
	char b[100];
	ifstream f("t3.4.txt");
	f.getline(b, 100);
	f.close();
	cout << endl << "file= " << b << endl;
	int l;
	l = sizeof(b);
	cout << "length= " << l << endl;
	cout << "numbers from file= ";
	for (int i = 0; i < l; i++)
	{  
	     if (b[i] == 48)
	     {
	     	cout << "0";
	     }
	     if (b[i] == 49)
	     {
	     	cout << "1";
	     }
	     if (b[i] == 50)
	     {
	     	cout << "2";
	     }
	     if (b[i] == 51)
	     {
	     	cout << "3";
	     }
	     if (b[i] == 52)
	     {
	     	cout << "4";
	     }
	     if (b[i] == 53)
	     {
	     	cout << "5";
	     }
	     if (b[i] == 54)
	     {
	     	cout << "6";
	     }
	     if (b[i] == 55)
	     {
	     	cout << "7";
	     }
	     if (b[i] == 56)
	     {
	     	cout << "8";
	     }
	     if (b[i] == 57)
	     {
	     	cout << "9";
	     }
	}
}