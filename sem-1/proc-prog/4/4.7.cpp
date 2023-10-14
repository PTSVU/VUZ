#include <iostream>

int main()
{
    setlocale(LC_ALL, "Russian");
    using namespace std;
    int m = 37, m1 = 25173;
    int b = 3, b1 = 13849;
    int c = 64, c1 = 65537;
    int s = 0, s1 = 0, p;
    cout << "Сколько раз вы хотите вывести(с 1 по какое число)= ";
    cin >> p;
    cout << endl;
    for (int i = 0; i < p; i++)
    {
        s = (((m * s) + b) % c);
        s1 = (((m1 * s1) + b1) % c1);
        cout << "variant 1, num " << i << "= " << s << endl << endl;
        cout << "variant 2, num " << i << "= " << s1 << endl << endl;
    }
}