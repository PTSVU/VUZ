#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ofstream t("t3.3.txt");
	string a;
	getline(cin, a);
	t << a;
	t.close();
	char b[1000000];
	ifstream f("t3.3.txt");
	f.getline(b, 1000000);
	f.close();
	cout << b << endl;
}