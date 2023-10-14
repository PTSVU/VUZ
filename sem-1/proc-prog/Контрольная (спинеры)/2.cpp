#include <iostream>
using namespace std;

int main()
{
    int m, t, f;
    cout << "count lopost= ";
    cin >> m;
    switch (m % 4)
    {
    case 0:
        {
            t = 0;
            f = m / 4;
            break;
        }
    case 1:
        {
            t = 3;
            f = (m - 9) / 4;
            break;
        }
    case 2:
        {
            t = 2;
            f = (m - 6) / 4;
            break;
        }
    case 3:
        {
            t = 1;
            f = (m - 3) / 4;
            break;
        }
    }
    if (m == 1 || m == 2 || m == 5)
    {
        cout << "0 0" << endl;
    }
    else
    {
        cout << t << " " << f << endl;
    }
    return 0;
}