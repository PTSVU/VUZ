#include <iostream>
using namespace std;

int main()
{
    double s, p=1, n, r, m;

    cout << "s= ";
    cin >> s;
    if (!s or s <= 0)
    {
        cout << "nope" << endl;
        return 0;
    }
    else
    {
        cout << "n= ";
        cin >> n;
        if (!n or n <= 0)
        {
            cout << "nope" << endl;
            return 0;
        }
        else
        {
            cout << "m= ";
            cin >> m;
            if (!m or m <= 0)
            {
                cout << "nope" << endl;
                return 0;
            }
            else
            {
                for (p = 1; p <= 100; p += 1)
                {
                    r = p / 100;
                    if ((s * r * pow(1 + r, n)) / (12 * (pow(1 + r, n) - 1)) > m)
                    {
                        cout << p << endl;
                        return 0;
                    }
                }
            }
        }
    }
}