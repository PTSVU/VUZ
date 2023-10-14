#include <iostream>
#include <time.h> 
using namespace std;

long long step_counter_mf = 0, step_counter_cf = 0;
double time_spent = 0.0; // переменная время

//Сортировка вставками  — алгоритм сортировки, в котором элементы входной последовательности просматриваются по одному,
//и каждый новый поступивший элемент размещается в подходящее место среди ранее упорядоченных элементов

void insertionSort(int numbers[], int num) // сортировка из википедии
{
    clock_t begin = clock(); // переменная для начала врмени

    int key, j;
    for (int i = 1; i < num; i++) // цикл проходов, i - номер прохода
    {
        key = numbers[i];
        j = i - 1;
        while (j >= 0 && numbers[j] > key) // поиск места элемента в готовой последовательности 
        {
            numbers[j + 1] = numbers[j]; // сдвигаем элемент направо, пока не дошли
            j = j - 1;

            step_counter_mf++; // СЧЁТЧИК ШАГОВ ПЕРЕМЕЩЕНИЯ  (МФ)
        }
        // место найдено, вставить элемент
        numbers[j + 1] = key;
        step_counter_cf++; // СЧЁТЧИК ШАГОВ (СФ)
    }

    clock_t end = clock(); // переменная для конца врмени
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;// подсчёт разницы времени между началом и концом

}

void printArray(int numbers[], int num) // цикл для вывода каждого элемента
{
    int i;
    for (i = 0; i < num; i++)
        cout << numbers[i] << " ";
    cout << endl;
}

int main()
{
    int num; // размер массива
    cout << "Enter value: ";
    cin >> num; // получение от пользователя размера массива

    int* numbers = new int[num]; // Выделение памяти для массива

    srand(time(0)); // инициализация генерации случайных чисел

    for (long i = 0; i < num; i++)   // заполнение массива
    {
        numbers[i] = 1 + rand() % num; // генерирование случайного числа
    }

    printArray(numbers, num);
    insertionSort(numbers, num);
    printArray(numbers, num);

    cout << "=========================" << endl;
    cout << "used time " << time_spent << endl;;
    cout << endl;
    cout << "=========================" << endl;
    cout << step_counter_mf << " mf " << endl;
    cout << step_counter_cf << " sf " << endl;
    cout << step_counter_mf + step_counter_cf << " " << "sf+mf" << endl;
    cout << "=========================" << endl;

    delete[] numbers; // очистка памяти
    return 0;
}