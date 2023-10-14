#include <iostream>
using namespace std;

int main()
{
    double x, y, b, z;
    cout << "x= " << endl;
    cin >> x;
    cout << "y= " << endl;
    cin >> y;
    cout << "b= " << endl;
    cin >> b;

    if (b - x < 0)
    {
        cout << "nope" << endl;
        return 0;
    }
    else
    {
        if (b - y <= 0)
        {
            cout << "nope" << endl;
            return 0;
        }
        else
        {
            z = (log(b - y)) * sqrt(b - x);
            cout << z << endl;
        }
    }
}