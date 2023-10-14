#include <iostream>
using namespace std;

int main()
{
    int a, b, c, n, n1;
    cout << "base price= ";
    cin >> a;
    cout << "price of one lopost= ";
    cin >> b;
    cout << "max price= ";
    cin >> c;
    if (a <= c)
    {
        n = (c - a) / b;
        cout << endl << "price= " << (a+b*n) << endl;
        cout << "lopost= " << n;
        return 0;
    }
    else
    {
        cout << "base price is too much";
        return 0;
    }
}