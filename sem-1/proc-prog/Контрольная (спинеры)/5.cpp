#include <iostream>
using namespace std;

int main()
{
	setlocale(0, "");
	system("chcp 1251 » null");
	unsigned long long int N, K, left, right, i1 = 0, i2 = 0, sum = 0, max = 0;
	cout << "Введите количество мест N в ряду: ";
	cin >> N;
	cout << "Введите количество школьников К: ";
	cin >> K;
	unsigned long long int * a = new unsigned long long int[N + 2];
	a[0] = 8; a[N + 1] = 8;
	for (unsigned long long int i = 1; i <= N; i++)
		a[i] = 0;
	while (K > 0)
	{
		for (unsigned long long int i = 0; i <= N + 1; i++)
		{
			if (a[i] == 0)
				sum = sum + 1;
			else
			{
				if (sum > max)
				{
					i1 = i - 1 - sum;
					i2 = i;
					max = sum;
				}
				sum = 0;
			}
		}
		a[(i1 + i2) / 2] = 2;
		sum = 0;
		max = 0;
		K = K - 1;
	}

	a[(i1 + i2) / 2] = 3;
	left = (i1 + i2) / 2 - (i1 + 1);
	right = (i2 - 1) - (i1 + i2) / 2;
	cout << endl << "Получившийся ряд: ";
	for (unsigned long long int i = 0; i <= N + 1; i++)
		cout << a[i] << " ";
	cout << endl << "Слева: " << left << endl << "Справа: " << right << endl;
	return 0;
}