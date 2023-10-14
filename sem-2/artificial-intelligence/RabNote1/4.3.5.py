import math


def calc(A, B, operation):
    if operation == 1:
        print("Результат операции 'A + B': ", A + B)
    elif operation == 2:
        print("Результат операции 'A - B': ", A - B)
    elif operation == 3:
        print("Результат операции 'A * B': ", A * B)
    elif operation == 4:
        print("Результат операции 'A / B': ", A / B)
    elif operation == 5:
        print("Результат операции 'e ^ (A + B)': ", math.e ** (A + B))
    elif operation == 6:
        print("Результат операции 'sin(A + B)': ", math.sin(A + B))
    elif operation == 7:
        print("Результат операции 'cos(A + B)': ", math.cos(A + B))
    elif operation == 8:
        print("Результат операции 'A ^ B': ", A ** B)
    else:
        print("Ошибка, введено не верное число\n")
        print(
            " 1= 'A + B'\n",
            "2= 'A - B'\n",
            "3= 'A * B'\n",
            "4= 'A / B'\n",
            "5= 'e ^ (A + B)'\n",
            "6= 'sin(A + B)'\n",
            "7= 'cos(A + B)'\n",
            "8= 'A ^ B'\n"
        )
        operation = int(input())
        calc(A, B, operation)


A = float(input())
B = float(input())
operation = int(input())
print(f" A= {A}\n", f"B= {B}\n")
calc(A, B, operation)
# %%
