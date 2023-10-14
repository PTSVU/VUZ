def func1(a): # Определить является ли заданное натуральное число простым.
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            print("False")
            return
    print("True")


def func2(list1): # В одномерном списке, состоящем из целых чисел, вычислите сумму элементов списка, расположенных между первым и последним отрицательными
    index1 = 0
    index2 = 0
    sum = 0
    for i in range(0, len(list1)):
        if list1[i] < 0:
            index1 = i
            break
    list2 = list1
    for j in range(len(list1) - 1, -1, -1):
        if list2[j] < 0:
            index2 = j
            break
    for i in range(index1 + 1, index2):
        sum += list1[i]
    print(sum)


def func3(list2): # В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.
    sum1 = 0
    sum2 = 0
    index = 0
    o = []
    for i in range(0, len(list2) - 1):
        if list2[i + 1] > list2[i]:
            sum1 += 1
        if list2[i + 1] < list2[i]:
            sum1 = 1
        if sum2 < sum1:
            sum2 = sum1
            index = i
    for i in range(0, sum2):
        o.append(list2[index-i+1])
    print(sum2)
    print(o[-1::-1])


print("Выберите вариант\n",
      "   1 - задача 1: Определить является ли заданное натуральное число простым.\n",
      "   2 - задача 2: В одномерном списке, состоящем из целых чисел, вычислите сумму элементов списка, расположенных между первым и последним отрицательными\n",
      "   3 - задача 3: В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.\n"
      )
var = int(input())
if var == 1:
    a = int(input("Введите число: "))
    func1(a)
if var == 2:
    list1 = [1, 2, -3, 4, 5, -1, -1, 2, 3, -3, 4]
    func2(list1)
if var == 3:
    list2 = [1, 2, -3, 4, 5, -2, -1, 2, 3, 13, 14, 15]
    func3(list2)