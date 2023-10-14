#include <iostream>
#include <cmath>

using namespace std;

bool IsPrime(int N)
{
    for (int i = 2; i <= sqrt(N); i++)
        if (N % i == 0)
        {
            return false;
        }
        if (N < 2)
        {
            return false;
        }
        return true;
}

int main()
{
    int a, b;
    cout << "prime numbers from number= ";
    cin >> a;
    cout << "prime numbers to number= ";
    cin >> b;
    cout << "range" << " from " << a << " to " << b << endl;
    for (int i = a; i <= b; i++)
    {
        if (IsPrime(i))
            cout << i << " ";
    }
    cout << endl;
    system("pause");
    return 0;
}