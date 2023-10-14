#include <iostream>
#include <fstream>
#include <string>
#pragma comment(linker, "/STACK:1073741824")
using namespace std;

double** addition(double** A, double** B, int size)
{
    double** result = new double* [size];

    for (int i = 0; i < size; i++)
    {
        result[i] = new double[size];
    }
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
    return result;
}

double** subtraction(double** A, double** B, int size)
{
    double** result = new double* [size];

    for (int i = 0; i < size; i++)
    {
        result[i] = new double[size];
    }
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            result[i][j] = A[i][j] - B[i][j];
        }
    }
    return result;
}

double** multiplicationByNumber(double** A, double number, int size)
{
    double** result = new double* [size];

    for (int i = 0; i < size; i++)
    {
        result[i] = new double[size];
    }
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            result[i][j] = A[i][j] * number;
        }
    }
    return result;
}

double** multiplication(double** A, double** B, int size)
{
    double** result = new double* [size];
    double sum;
    for (int i = 0; i < size; i++)
    {
        result[i] = new double[size];
    }
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            sum = 0;
            for (int k = 0; k < size; k++)
            {
                sum += A[i][k] * B[k][j];
            }
            result[i][j] = sum;
        }
    }
    return result;
}

int main()
{
    double** A;
    double** B;
    double** C;
    double** E;
    double** M;

    int n;
    cout << "Input matrix size= ";
    cin >> n;
    if (n > 1)
    {
        cout << "Initialize A" << endl;
        A = new double* [n];
        for (int i = 0; i < n; i++)
        {
            A[i] = new double[n];
        }
        for (int i = 0; i < n; i++)
        {
            cout << "Input " << i << " row" << endl;
            for (int j = 0; j < n; j++)
            {
                cin >> A[i][j];
            }
        }
        cout << endl << "Initialize B" << endl;
        B = new double* [n];
        for (int i = 0; i < n; i++)
        {
            B[i] = new double[n];
        }
        for (int i = 0; i < n; i++)
        {
            cout << "Input " << i << " row" << endl;
            for (int j = 0; j < n; j++)
            {
                cin >> B[i][j];
            }
        }
        C = new double* [n];
        for (int i = 0; i < n; i++)
        {
            C[i] = new double[n];
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                C[i][j] = 1.0 / (i + 1 + j + 1);
            }
        }
        E = new double* [n];
        for (int i = 0; i < n; i++)
        {
            E[i] = new double[n];
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == j)
                {
                    E[i][j] = 1;
                }
                else
                {
                    E[i][j] = 0;
                }
            }
        }
        M = multiplication(A, subtraction(B, E, n), n);
        M = addition(M, C, n);
        cout << endl << endl;
        //вывод матриц
        ofstream o1("t5.5.O.txt");
        o1 << "Matrix A= " << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                o1 << A[i][j] << " ";
            }
            o1 << endl;
        }
        o1 << endl;
        o1 << "Matrix B= " << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                o1 << B[i][j] << " ";
            }
            o1 << endl;
        }
        o1 << endl;
        o1 << "Matrix C= " << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                o1 << C[i][j] << " ";
            }
            o1 << endl;
        }
        o1 << endl;
        o1 << "Matrix E= " << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                o1 << E[i][j] << " ";
            }
            o1 << endl;
        }
        o1 << endl;
        o1 << "Matrix M= " << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                o1 << M[i][j] << " ";
            }
            o1 << endl;
        }
        o1 << endl;
        o1.close();
        char o2[1000000];
        ifstream o3("t5.5.O.txt");
        while (o3)
        {
            o3.getline(o2, 1000000);
            cout << o2 << endl << endl;
        }
        o3.close();
    }
    else
    {
        cout << "min size = 2" << endl;
    }
    system("pause");
}