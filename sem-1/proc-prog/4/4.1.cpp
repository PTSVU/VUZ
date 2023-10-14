#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream t("4.1.txt");
    int n = 10, v, sum = 0, i = 1;
    for (i; i <= n; i++)
    {
        cout << "number" << i << "/10= ";
        cin >> v;
        t << v << endl;
    }
    t.close();
    ifstream t1("4.1.txt");
    for (i = 1; i <= n; i++)
    {
        t1 >> v;
        sum = sum + v;
    }
    cout << sum << endl;
}