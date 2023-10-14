// Сортировка вставками для двусвязного списка

#include <iostream>
#include <stdlib.h>
using namespace std;
// Узел двусвязного списка
struct Node
{
    int data;
    struct Node* prev, * next;
};

// функция для создания и возврата нового узла двусвязного списка
struct Node* getNode(int data)
{
    // выделить узел
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    // ввод в data
    newNode->data = data;
    newNode->prev = newNode->next = NULL;
    return newNode;
}

// функция для вставки нового узла отсортированным образом в отсортированный двусвязный список
void sortedInsert(struct Node** head_ref, struct Node* newNode)
{
    struct Node* current;

    // если список пуст
    if (*head_ref == NULL)
        *head_ref = newNode;

    // если узел должен быть вставлен в начало двусвязного списка
    else if ((*head_ref)->data >= newNode->data)
    {
        newNode->next = *head_ref;
        newNode->next->prev = newNode;
        *head_ref = newNode;
    }

    else
    {
        current = *head_ref;

        // найти узел, после которого должен быть вставлен новый узел
        while (current->next != NULL && current->next->data < newNode->data)
            current = current->next;

        /* делает соответствущие ссылки */

        newNode->next = current->next;

        // если новый узел не вставлен в конец списка
        if (current->next != NULL)
            newNode->next->prev = newNode;

        current->next = newNode;
        newNode->prev = current;
    }
}

// функция для сортировки двусвязного списка с использованием сортировки вставками
void insertionSort(struct Node** head_ref)
{
    // Инициализировать 'sorted' — отсортированный двусвязный список
    struct Node* sorted = NULL;

    // Пройдите по заданному двусвязному списку и вставьте каждый узел в 'sorted'
    struct Node* current = *head_ref;
    while (current != NULL) {

        // Сохранить рядом для следующей итерации
        struct Node* next = current->next;

        // удаление всех ссылок, чтобы создать 'current' как новый узел для вставки
        current->prev = current->next = NULL;

        // вставить текущий в 'sorted' двусвязный список
        sortedInsert(&sorted, current);

        // Обновить 'current'
        current = next;
    }

    // Обновите head_ref, чтобы он указывал на отсортированный двусвязный список
    *head_ref = sorted;
}

// функция для печати двусвязного списка
void printList(struct Node* head)
{
    while (head != NULL)
    {
        cout << head->data << " ";
        head = head->next;
    }
}

// функция для вставки узла в начало двусвязного списка
void push(struct Node** head_ref, int new_data)
{
    /* выделить узел */
    struct Node* new_node =
        (struct Node*)malloc(sizeof(struct Node));

    /* ввести данные */
    new_node->data = new_data;

    /* Сделать следующий новый узел головным, а предыдущий - NULL */
    new_node->next = (*head_ref);
    new_node->prev = NULL;

    /* изменить предыдущий узел головы на новый узел */
    if ((*head_ref) != NULL)
        (*head_ref)->prev = new_node;

    /* переместите голову, чтобы указать на новый узел */
    (*head_ref) = new_node;
}

// Программа-драйвер для проверки кода выше
int main()
{
    /* начать с пустого двусвязного списка */
    struct Node* head = NULL;
    int c = 1, i;
    // вставьте следующие данные
    cout << "if you want to stop entering numbers, then you need to enter a letter" << endl;
    while (c > 0)
    {
        cout << "numbers= ";
        cin >> i;
        if (!i)
        {
            c = 0;
        }
        else
        {
            push(&head, i);
        }
    }

    cout << endl << "no sort= " << "' ";
    printList(head);
    cout << "' " << endl << endl;

    insertionSort(&head);

    cout << "sort= " << "' ";
    printList(head);
    cout << "' " << endl << endl;

    return 0;
}