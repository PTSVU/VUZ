#include <iostream>
using namespace std;

int main()
{
    int num;
    int count = 0;
    cout << "number= ";
    cin >> num;
    if (!num)
    {
        cout << "seriously?" << endl;
        return 0;
    }
    else
    {
        cout << count << ") " << num << endl;
        while (count < 10)
        {
            num += 1;
            count += 1;
            cout << count << ") " << num << endl;
        }
    }
}