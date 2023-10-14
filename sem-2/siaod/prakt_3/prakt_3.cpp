#include <iostream>
#include <time.h> 
using namespace std;

long long step_counter_mf = 0, step_counter_cf = 0;
double time_spent = 0.0;

void MergeSort(int numbers[], int num)
{
	clock_t begin = clock();
	int BlockSizeIterator;
	int BlockIterator;
	int LeftBlockIterator;
	int RightBlockIterator;
	int MergeIterator;

	int LeftBorder;
	int MidBorder;
	int RightBorder;
	for (BlockSizeIterator = 1; BlockSizeIterator < num; BlockSizeIterator *= 2)
	{
		for (BlockIterator = 0; BlockIterator < num - BlockSizeIterator; BlockIterator += 2 * BlockSizeIterator)
		{
			//Производим слияние с сортировкой пары блоков начинающуюся с элемента BlockIterator
			//левый размером BlockSizeIterator, правый размером BlockSizeIterator или меньше
			LeftBlockIterator = 0;
			RightBlockIterator = 0;
			LeftBorder = BlockIterator;
			MidBorder = BlockIterator + BlockSizeIterator;
			RightBorder = BlockIterator + 2 * BlockSizeIterator;
			RightBorder = (RightBorder < num) ? RightBorder : num;
			int* SortedBlock = new int[RightBorder - LeftBorder];

			//Пока в обоих массивах есть элементы выбираем меньший из них и заносим в отсортированный блок
			while (LeftBorder + LeftBlockIterator < MidBorder && MidBorder + RightBlockIterator < RightBorder)
			{

				if (numbers[LeftBorder + LeftBlockIterator] < numbers[MidBorder + RightBlockIterator])
				{
					SortedBlock[LeftBlockIterator + RightBlockIterator] = numbers[LeftBorder + LeftBlockIterator];
					LeftBlockIterator += 1;
				}
				else
				{
					SortedBlock[LeftBlockIterator + RightBlockIterator] = numbers[MidBorder + RightBlockIterator];
					RightBlockIterator += 1;
				}
				step_counter_cf++;
			}
			//После этого заносим оставшиеся элементы из левого или правого блока
			while (LeftBorder + LeftBlockIterator < MidBorder)
			{
				SortedBlock[LeftBlockIterator + RightBlockIterator] = numbers[LeftBorder + LeftBlockIterator];
				LeftBlockIterator += 1;
			}
			while (MidBorder + RightBlockIterator < RightBorder)
			{
				SortedBlock[LeftBlockIterator + RightBlockIterator] = numbers[MidBorder + RightBlockIterator];
				RightBlockIterator += 1;
			}

			for (MergeIterator = 0; MergeIterator < LeftBlockIterator + RightBlockIterator; MergeIterator++)
			{
				numbers[LeftBorder + MergeIterator] = SortedBlock[MergeIterator];
				step_counter_mf++;
			}
			delete[] SortedBlock;
		}
	}
	clock_t end = clock();
	time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
}

void printArray(int numbers[], int num)
{
    int i;
    for (i = 0; i < num; i++)
        cout << numbers[i] << " ";
    cout << endl << endl;
}

int main()
{
    
    int num;
    cout << "Enter value: ";
    cin >> num;
    

    int* numbers = new int[num];

    srand(time(0));

    for (long i = 0; i < num; i++)
    {
        numbers[i] = 1 + rand() % num;
    }


    printArray(numbers, num);
	MergeSort(numbers, num);
    printArray(numbers, num);

    
	cout << endl << endl;
	cout << "MF= " << step_counter_mf/2 << endl;
	cout << "CF= " << step_counter_cf/2 << endl << endl;
	cout << "summ= " << (step_counter_mf + step_counter_cf)/2 << endl << endl;
    cout << "used time= " << time_spent << endl;


    delete[] numbers;
}