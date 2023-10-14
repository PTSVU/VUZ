#include <iostream>
#include <typeinfo>
using namespace std;

int main()
{

  double pi = 3.14;
  double R;
  double r;
  double L;
  double h;
  
  cout << "R= " << endl;
  cin >> R;
  if (!R)
  {
  	cout << "nope" << endl;
  	return 0;
  }
  else
  {
  	cout << "r= " << endl;
  	cin >> r;
  	if (!r)
  	{
  		cout << "nope" << endl;
  		return 0;
  	}
  	else
  	{
  		cout << "h= " << endl;
  		cin >> h;
  		if (!h)
  		{
  			cout << "nope" << endl;
  			return 0;
  		}
  		else
  		{
  			L = sqrt(((R - r) * (R - r)) + (h * h));
  			cout << "L= " << L << endl;
  			cout << "V= " << 1.0 / 3.0 * pi * h * ((R * R) + (R * r) + (r * r)) << endl;
  			cout << "S= " << pi * ((R * R) + (R + r) * L + (r * r)) << endl;
  		}
  	}
  }
}