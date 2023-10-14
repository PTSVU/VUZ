#include "func.h"

int main()
{
	int num, search_num;
	cout << "Enter value: ";
	cin >> num;
	cout << "Search num from " << 1 << " for " << num << "= ";
	cin >> search_num;
	prin = 1;
	prin_bar = 1;


	int* numbers = new int[num];

	RandMas(numbers, num);
	Search(numbers, num, search_num);
	IncreaseMas(numbers, num);
	Search(numbers, num, search_num);
	DescendingMas(numbers, num);
	Search(numbers, num, search_num);
}