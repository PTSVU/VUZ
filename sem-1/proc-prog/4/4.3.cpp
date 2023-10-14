#include <iostream>
using namespace std;

double a, h, r, S;
double triangles()
{
    cout << "enter the height and base of the triangle" << endl;
    cout << "height= ";
    cin >> h;
    cout << "base = ";
    cin >> a;
    S = h * a / 2;
    return S;
}

double rectangles()
{
    cout << "enter the height and base of the rectangle" << endl;
    cout << "height= ";
    cin >> h;
    cout << "base= ";
    cin >> a;
    S = a * h;
    return S;
}

double circles()
{
    cout << "enter the radius of the circle" << endl;
    cout << "radius= ";
    cin >> r;
    S = 3.14 * r * r;
    return S;
}

int main()
{
    string triangle = "t", rectangle = "r", circle = "c", shapes;
    cout << "available shapes : triangle(t), rectangle(r), circle(c)" << endl;
    cout << "enter the figure whose area (S) you want to find" << endl;
    cin >> shapes;
    if (shapes == triangle)
    {
        cout << triangles() << endl;
    }
    if (shapes == rectangle)
    {
        cout << rectangles() << endl;
    }
    if (shapes == circle)
    {
        cout << circles() << endl;
    }
    system("pause");
}