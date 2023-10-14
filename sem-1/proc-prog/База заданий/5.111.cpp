#include <stdlib.h>
#include <iostream>
using namespace std;

int nopr = 0;

void put(int from, int to)
{
    cout << from << " => " << to << " | ";
    if (0 == (++nopr % 5))
    {
        cout << endl;
    }
}

void move(int from, int to, int n)
{
    int temp = from ^ to;
    if (1 == n)
    {
        put(from, to);
    }
    else
    {
        move(from, temp, n - 1);
        put(from, to);
        move(temp, to, n - 1);
    }
}

int main(int argc, char** argv, char** envp)
{
    int n;
    cout << "disk num= ";
    cin >> n;
    if (argc > 1 and atoi(argv[1]) != 0)
    {
        n = atoi(argv[1]);
    }
    cout << "town size= " << n << endl;
    move(1, 3, n);
    if (0 != (nopr % 5))
    {
        cout << endl;
    }
    cout << "num movements= " << nopr << endl;
    system("pause");
}