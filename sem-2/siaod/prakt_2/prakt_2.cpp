#include <iostream>
#include <time.h> 
using namespace std;

long long step_counter_mf = 0, step_counter_cf = 0;
double time_spent = 0.0; // переменная время

// QuickSort является существенно улучшенным вариантом алгоритма сортировки с помощью прямого обмена («Пузырьковая сортировка» и «Шейкерная сортировка»)
// в первую очередь производятся перестановки на наибольшем возможном расстоянии и после каждого прохода элементы делятся на две независимые группы
// 
// из массива выбирается некоторый опорный элемент a[i]
// запускается процедура разделения массива, которая перемещает все ключи, меньшие, либо равные a[i], влево от него, а все ключи, большие, либо равные a[i] - вправо
// теперь массив состоит из двух подмножеств, причем левое меньше, либо равно правого
// для обоих подмассивов : если в подмассиве более двух элементов, рекурсивно запускаем для него ту же процедуру

void qsort(int numbers[], int num)
{
    clock_t begin = clock(); // переменная для начала врмени

    int i = 0;
    int j = num - 1; // переменная для счёта с конца
    int mid = numbers[num / 2]; // переменная для определения середины
    do {
        //Пробегаем элементы, ищем те, которые нужно перекинуть в другую часть
        //В левой части массива пропускаем(оставляем на месте) элементы, которые меньше центрального
        while (numbers[i] < mid) { 
            i++;
            step_counter_cf++;  // СЧЁТЧИК ШАГОВ(СФ)
        }
        //В правой части пропускаем элементы, которые больше центрального
        while (numbers[j] > mid) {
            j--;
            step_counter_cf++;  // СЧЁТЧИК ШАГОВ(СФ)
        }
        //Меняем элементы местами
        if (i <= j) {
            int tmp = numbers[i]; // tmp-временная переменная 
            numbers[i] = numbers[j]; 
            numbers[j] = tmp;

            i++;
            j--;
            step_counter_mf++;  // СЧЁТЧИК ШАГОВ ПЕРЕМЕЩЕНИЯ  (МФ)
        }
    } while (i <= j);
    //Рекурсивные вызовы, если осталось, что сортировать
    if (j > 0) {
        // Левый кусок
        qsort(numbers, j + 1);
    }
    if (i < num) {
        // Правый кусок
        qsort(&numbers[i], num - i);
    }

    clock_t end = clock(); // переменная для конца врмени
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC; // подсчёт разницы времени между началом и концом
}

void printArray(int numbers[], int num)  // цикл для вывода каждого элемента
{
    int i;
    for (i = 0; i < num; i++)
        cout << numbers[i] << " ";
    cout << endl << endl;
}

int main()
{
    int num; // размер массива
    cout << "Enter value: ";
    cin >> num; // получение от пользователя размера массива

    int* numbers = new int[num]; // Выделение памяти для массива

    srand(time(0)); //для отчистки псевдорандома

    for (long i = 0; i < num; i++) // заполнение массива
    {
        numbers[i] = 1 + rand() % num; // генерирование случайного числа
    }

    printArray(numbers, num);
    qsort(numbers, num);
    printArray(numbers, num);

    cout << endl << endl << "MF= " << step_counter_mf << endl << "CF= " << step_counter_cf << endl << endl << "summ= " << step_counter_mf + step_counter_cf << endl << endl << endl;
    cout << endl << endl << "used time= " << time_spent;

    delete[] numbers; // очистка памяти
    return 0;
}