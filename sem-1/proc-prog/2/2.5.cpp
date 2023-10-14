#include <iostream>
using namespace std;

int main()
{
    double x, y;
    int count = 0;

    for (x = -4; x <= 4; x += 0.5)
    {
        count = count + 1;
        y = (x * x - 2 * x + 2) / (x - 1);
        if (x - 1 == 0)
        {
            cout << count << ") " << "in " << x << endl << "    we have " << "nope" << endl;
        }
        else if (x == 0)
        {
            y = 2/-1;
            cout << count << ") " << "in " << x << endl << "    we have " << y << endl;
        }
        else
        {
            cout << count << ") " << "in " << x << endl << "    we have " << y << endl;
        }

    }
}