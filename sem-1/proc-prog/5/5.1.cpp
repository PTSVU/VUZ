#include <iostream>

using namespace std;

int NOD(int a, int b)
{
    //вариант делением
    while (a != 0 and b != 0)
    {
        if (a > b)
        {
            a = a % b;
        }
        else
        {
            b = b % a;
        }
    
    }
    return (a + b);
    //вариант вычетанием
    while (a != b)
    {
        if (a > b)
        {
            a = a - b;
        }
        else
        {
            b = b - a;
        }

    }
    return (a);
}


int main(void)
{
    cout << NOD(30, 18) << endl;
}