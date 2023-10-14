#include <iostream>
using namespace std;

int main()
{

  int light;
  int shtor;
  int san;
  
  cout << "  (1=yes  0=no) " << endl;
  cout << " Light turn on? " << endl;
  cin >> light;
  cout << " Curtains open? " << endl;
  cin >> shtor;
  cout << " Sun? " << endl;
  cin >> san;

  if (light == 1  or shtor == 1 and san == 1)
  {
    cout << " It's light " << endl;
    return 0;
  }
  else
  {
    cout << " It's dark " << endl;
    return 0;
  }
}