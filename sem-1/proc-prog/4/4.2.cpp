#include <iostream>
using namespace std;

int x;
int Sign(int x)
{
    if (x == 0)
    {
        return 0;
    }
    if (x > 0)
    {
        return 1;
    }
    else
    {
        return -1;
    }
}
int main()
{
    cin >> x;
    int Rezult = Sign(x);
    cout << Rezult << endl;
    return 0;
}