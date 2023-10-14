#include <iostream>
#include <time.h>
using namespace std;

long long step_counter_cf = 0;
double time_spent_a = 0.0, time_spent_b = 0.0;
int prin, prin_bar;


void Search(int numbers[], int num, int search_num);
void Print(int numbers[], int num);
void RandMas(int numbers[], int num);
void IncreaseMas(int numbers[], int num);
void DescendingMas(int numbers[], int num);


void Search(int numbers[], int num, int search_num)
{
	if (prin_bar == 1)
	{
		numbers[num - 1] = search_num;
		Print(numbers, num);
	}
	else
	{
		Print(numbers, num);
		numbers[num - 1] = search_num;
	}
	
	bool suc = false;
	clock_t begin = clock();
	for (int i = 0; i < num - 1; i++)
	{
		if (numbers[i] == search_num)
		{
			clock_t end = clock();
			time_spent_a += (double)(end - begin) / CLOCKS_PER_SEC;
			cout << "\n\tYou found number";
			cout << "\n\tCF= " << i + 1;
			cout << "\n\tTime= " << time_spent_a << "\n\n";
			suc = true;
			break;
		}
	}
	if (suc == false)
	{
		clock_t end = clock();
		time_spent_a += (double)(end - begin) / CLOCKS_PER_SEC;
		cout << "\n\tYou not found number";
		cout << "\n\tTime= " << time_spent_a << "\n\n";
	}
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

void IncreaseMas(int numbers[], int num)
{
	for (int i = 0; i < num; i++)
	{
		numbers[i] = i + 1;
	}
	cout << "\nIncreaseMas:\n";
}

void DescendingMas(int numbers[], int num)
{
	for (int i = num, j = 0; (i > 0) and (j < num); i--, j++)
	{
		numbers[j] = i;
	}
	cout << "\nDescendingMas:\n";
}