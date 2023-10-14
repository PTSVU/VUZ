#include <iostream>
using namespace std;

int main()
{
    double m, s, n, p, r;

    cout << "s= ";
    cin >> s;
    if (s != !s and s != 0)
    {
        cout << "n= ";
        cin >> n;
        if (n != !n and n != 0)
        {
            cout << "p= ";
            cin >> p;
            if (p != !p and p != 0)
            {
                r = p / 100;
                m = ((s * r) * pow((1 + r), n)) / (12 * (pow((1 + r), n) - 1));
                cout << m << endl;
            }
            else
            {
                cout << "nope" << endl;
                return 0;
            }
        }
        else
        {
            cout << "nope" << endl;
            return 0;
        }
    }
    else
    {
        cout << "nope, it doesn't actually work" << endl << "or do you think otherwise?" << endl << endl << "no, it can't be truth" << endl;
        return 0;
    }
}