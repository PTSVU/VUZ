#include <iostream>
#include <algorithm>
#include <chrono>
#pragma comment(linker, "/STACK:1073741824")
using namespace std;

bool perestanovka(int* urna, int n)
{
    for (int i = 0; i < n; ++i)
    {
        if (urna[i] == i)
        {
            return true;
        }
    }
    return false;
}

long double factorial(long double fac)
{
    if (fac == 0) return 1;
    else return fac * factorial(fac - 1);
}


int main()
{
    auto begin = chrono::steady_clock::now();
    int n;
    long double fac;
    cout << "enter number of permutations(the number from which the factorial is required)= ";
    cin >> n;
    fac = factorial(n);
    int urna[100] = { 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99 };
    if (n > 12)
    {
        long double ans = 0;
        for (int i = 0; i < fac; ++i)
        {
            next_permutation(urna, urna + n);
            if (perestanovka(urna, n))
                ans++;
        }
        cout << "rezult= " << ans << endl;
    }
    else
    {
        int ans = 0;
        for (int i = 0; i < fac; ++i)
        {
            next_permutation(urna, urna + n);
            if (perestanovka(urna, n))
                ans++;
        }
        cout << "rezult= " << ans << endl;
    }
    auto end = chrono::steady_clock::now();
    auto elapsed_ms = chrono::duration_cast<chrono::milliseconds>(end - begin);
    cout << "The time: " << elapsed_ms.count() << " ms\n";
}