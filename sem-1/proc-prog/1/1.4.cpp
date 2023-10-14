#include <iostream>
using namespace std;

int main()
{
  double x1, x2, x3, x4, a, b, c, D;

  cout << "a= ";
  cin >> a;
  cout << "b= ";
  cin >> b;
  cout << "c= ";
  cin >> c;

  D = b * b - 4 * a * c;

  if (D > 0)
  {
    x1 = (-b + (sqrt(D))) / (2 * a);
    x2 = (-b - (sqrt(D))) / (2 * a);
    
    if (2 * a == 0 and D != 0)
    {
      x1 = -c / b;
      if (x1 == -0)
      {
      	x4 = x1 + 0;
      	cout << "x1= " << x4 << endl;
      }
      else
      {
      	cout << "x1= " << x1 << endl;
      }
    }
    else if (2 * a == 0)
    {
      cout << "nope" << endl;
    }
    else
    {
      cout << "x1= " << x1 << endl;
      cout << "x2= " << x2 << endl; 
    } 
  }
  else if (D == 0)
  {
    if (2 * a == 0)
    {
      cout << "nope" << endl;
    }
    else
    {
      x3 = (-b) / (2 * a);
      cout << "x1= " << x3 << endl;
    }
  }
  else
  {
    cout << "nope" << endl;
  }
}