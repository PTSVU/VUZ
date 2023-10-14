#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N;
    string c;
    cin >> N;
    if (!N || N > 9)
    {
        cout << "N is wrong: " << N;
    }
    else
    {
        for (int i = 1; i <= N; i++)
        {
            c = c + to_string(i);
            cout << c;
            c = c + " ";
            if (i != N)
            {
                cout << endl;
            }
        }
    }
}