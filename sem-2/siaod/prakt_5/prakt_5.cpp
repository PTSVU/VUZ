#include <iostream>
#include <algorithm>
using namespace std;

long long step_counter_cf = 0;
double time_spent;
int prin;

void Print(int numbers[], int num);

void BinSearch(int numbers[], int num, int search_num)
{
	sort(numbers, numbers + num);
	Print(numbers, num);
	int l = 0, r = num-1, mid;
	bool suc = false;
	clock_t begin = clock();

	while ((l <= r) && (suc != true))
	{
		mid = (l + r) / 2;

		if (numbers[mid] == search_num)
		{
			suc = true;
		}
		if (numbers[mid] > search_num)
		{
			r = mid - 1;
		}
		else
		{
			l = mid + 1;
		}
		step_counter_cf++;
	}

	if (suc)
	{
		cout << "\n\tIndex " << search_num << " in mas= " << mid;
		cout << "\n\tCF= " << step_counter_cf;
	}
	else
	{
		cout << "\n\tYou not found number";
	}

	clock_t end = clock();
	time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
	cout << "\n\tTime= " << time_spent << "\n\n";
}

void Print(int numbers[], int num)
{
	if (prin == 1)
	{
		cout << "\nMas= ";
		for (int i = 0; i < num; i++)
		{
			cout << numbers[i] << " ";
		}
		cout << "\n\n";
	}
	else
	{
		cout << "\nMas not print\n";
	}
}

void RandMas(int numbers[], int num)
{
	srand(time(NULL));
	for (long i = 0; i < num; i++)
	{
		numbers[i] = 1 + rand() % num;
	}
	cout << "\nRandom mas:\n";
}

int main()
{
	int num, search_num;
	cout << "Enter value: ";
	cin >> num;
	cout << "Search num from " << 1 << " for " << num << "= ";
	cin >> search_num;
	cout << "Print mas?\n\t1 - Yes\n\t2 - No\n";
	cin >> prin;

	int* numbers = new int[num];

	RandMas(numbers, num);
	BinSearch(numbers, num, search_num);
	delete[]numbers;
}