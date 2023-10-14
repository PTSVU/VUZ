#include <iostream>
using namespace std;

void MultiplyWithOutAMP()
{
    double aMatrix[3][4] = { {5, 2, 0, 10}, {3, 5, 2, 5}, {20, 0, 0, 0} };
    double bMatrix[4][2] = { {1.20, 0.50}, {2.80, 0.40}, {5.00, 1.00}, {2.00, 1.50} };
    double product[3][2] = { {0.0, 0.0}, {0.0, 0.0}, {0.0, 0.0} };

    for (int row = 0; row < 3; row++)
    {
        for (int col = 0; col < 2; col++)
        {
            // Multiply the row of A by the column of B to get the row, column of product.
            for (int inner = 0; inner < 4; inner++)
            {
                product[row][col] += aMatrix[row][inner] * bMatrix[inner][col];
            }
            cout << product[row][col] << "  ";
        }
        cout << "\n";
    }
    //задание 1.1
    double o11 = 0;
    int o111 = 0;
    for (int n = 0; n < 3; n++)
    {
        if (product[n][0] > o11)
        {
            o11 = product[n][0];
            if (n == 0)
            {
                o111 = 1;
            }
            else if (n == 1)
            {
                o111 = 2;
            }
            else if (n == 2)
            {
                o111 = 3;
            }
        }
    }
    cout << endl << "#1.1" << endl;
    cout << "max trader= " << o111 << " his max= " << o11 << endl << endl;
    //задание 1.2
    double o12 = 1000000;
    int o121 = 0;
    for (int n = 0; n < 3; n++)
    {
        if (product[n][0] < o12)
        {
            o12 = product[n][0];
            if (n == 0)
            {
                o121 = 1;
            }
            else if (n == 1)
            {
                o121 = 2;
            }
            else if (n == 2)
            {
                o121 = 3;
            }
        }
    }
    cout << "#1.2" << endl;
    cout << "min trader= " << o121 << " his min= " << o12 << endl << endl;
    //задание 2.1
    double o21 = 0;
    int o211 = 0;
    for (int n = 0; n < 3; n++)
    {
        if (product[n][1] > o21)
        {
            o21 = product[n][1];
            if (n == 0)
            {
                o211 = 1;
            }
            else if (n == 1)
            {
                o211 = 2;
            }
            else if (n == 2)
            {
                o211 = 3;
            }
        }
    }
    cout << endl << "#2.1" << endl;
    cout << "max trader= " << o211 << " his max= " << o21 << endl << endl;
    //задание 2.2
    double o22 = 1000000;
    int o221 = 0;
    for (int n = 0; n < 3; n++)
    {
        if (product[n][1] < o22)
        {
            o22 = product[n][1];
            if (n == 0)
            {
                o221 = 1;
            }
            else if (n == 1)
            {
                o221 = 2;
            }
            else if (n == 2)
            {
                o221 = 3;
            }
        }
    }
    cout << "#2.2" << endl;
    cout << "min trader= " << o221 << " his min= " << o22 << endl << endl;
    //задание 3
    double o3 = 0;
    for (int n = 0; n < 3; n++)
    {
        o3 = o3 + product[n][0];
    }
    cout << endl << "#3" << endl;
    cout << "sum prib= " << o3 << endl << endl;
    //задание 4
    double o4 = 0;
    for (int n = 0; n < 3; n++)
    {
        o4 = o4 + product[n][1];
    }
    cout << endl << "#4" << endl;
    cout << "sum comis= " << o4 << endl << endl;
    //задание 5
    double o5 = 0;
    for (int n = 0; n < 3; n++)
    {
        o5 = o5 + (product[n][0] + product[n][1]);
    }
    cout << endl << "#5" << endl;
    cout << "sum dengi= " << o5 << endl << endl;
}

int main()
{
    MultiplyWithOutAMP();
    getchar();
}