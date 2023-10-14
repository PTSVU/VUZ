#include <iostream>
using namespace std;

int main()
{
    double a, x, w;
    cout << "x= ";
    cin >> x;
    cout << "a= ";
    cin >> a;
    if (abs(x) < 1 and abs(x) != 0)
    {
        w = a * log(abs(x));
        if (a != 0)
        {
            cout << "w= " << w << endl;
        }
        else
        {
            cout << "0" << endl;
        }
    }
    else if (abs(x) >= 1)
    {
        if (a < (pow(x, 2)))
        {
            cout << "nope" << endl;
            return 0;
        }
        else
        {
            w = sqrt(a - pow(x, 2));
            cout << "w= " << w << endl;
        }
    }
    else
    {
        cout << "nope" << endl;
        return 0;
    }
}