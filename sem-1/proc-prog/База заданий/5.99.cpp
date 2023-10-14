#include <iostream>
using namespace std;

int main()
{
	int num1[4], num2[4], xod = 0, p, m;
	srand(time(NULL));
	for (int i = 0; i < 4; i++)
	{
		int ch;
		ch = rand() % 9 + 0;
		num1[i] = ch;
		if ((num1[0] == num1[1]) or (num1[0] == num1[2]) or (num1[0] == num1[3]))
		{
			do
			{
				ch = rand() % 9 + 0;
				num1[i] = ch;
			} while ((num1[0] == num1[1]) or (num1[0] == num1[2]) or (num1[0] == num1[3]));
		}
		if (((num1[1] == num1[2]) or (num1[1] == num1[3])) and (i >= 1))
		{
			do
			{
				ch = rand() % 9 + 0;
				num1[i] = ch;
			} while ((num1[1] == num1[2]) or (num1[1] == num1[3]));
		}
		if ((num1[2] == num1[3]) and (i >= 2))
		{
			do
			{
				ch = rand() % 9 + 0;
				num1[i] = ch;
			} while ((num1[2] == num1[3]));
		}
	}
	cout << "Nums= " << num1[0] << num1[1] << num1[2] << num1[3] << endl << endl;

	do
	{
		xod++;
		for (int s = 0; s < 4; s++)
		{
			cout << "Your num " << s+1 <<"= ";
			cin >> num2[s];
			while (num2[s] < 0)
			{
				cout << endl << "Don't enter negative number" << endl << "Your num " << s + 1 << "= ";
				cin >> num2[s];
			}
		}
		p = 0;
		m = 0;
		for (int i = 0; i < 4; i++)
		{
			if (num2[i] == num1[i])
			{
				p++;
			}
			else
			{
				for (int j = 0; j < 4; j++)
				{
					if (num2[j] == num1[i])
					{
						m++;
					}
				}
			}
		}
		cout << endl << "Plus= " << p << endl << "Minus= " << m << endl << endl;
	} while (p != 4);

	cout << endl << "Number of moves to win " << xod << endl << endl;
	system("pause");
}