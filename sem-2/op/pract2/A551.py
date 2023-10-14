# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определенном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.

market = [
          {"id": 1, "product": "Колла", "department": "Напитки"},
          {"id": 2, "product": "Вода", "department": "Напитки"},
          {"id": 3, "product": "Чипсы", "department": "Еда"},
          {"id": 4, "product": "Олежа", "department": "Сотрудники"},
          {"id": 5, "product": "Печеньки", "department": "Еда"},
          {"id": 6, "product": "Мороженое", "department": "Холодное"},
          {"id": 7, "product": "Сникерс", "department": "Еда"},
          {"id": 8, "product": "Курица", "department": "Холодное"},
          {"id": 9, "product": "Кассирша", "department": "Сотрудники"},
          {"id": 10, "product": "Пиво", "department": "Напитки"},
          {"id": 11, "product": "NULL", "department": "NULL"}
          ]


def Print_All():
    [[print(i, _.get(i)) for i in _.keys()] for _ in market]
    print("\n\n")


def Print_ID(ID):
    for i in market:
        if i['id'] == ID:
            [print(_, i.get(_)) for _ in i.keys()]
    print("\n\n")


def Print_Dep(department):
    summ = 0
    for i in market:
        if i["department"] == department:
            summ = summ + 1
    print(summ, "\n\n")


def Update(ID):
    for i in market:
        if i['id'] == ID:
            name = str(")")
    departmentName = str("))")
    i2 = {"id": i['id'], "product": name, "department": departmentName}
    i.update(i2)
    [print(_, i.get(_)) for _ in i.keys()]
    print("\n")


def Dele(ID):
    for i in range(len(market)):
        if market[i]['id'] == ID:
            market.pop(i)
            break
    [[print(i, _.get(i)) for i in _.keys()] for _ in market]


Print_All()
Print_ID(4)
Print_Dep("Сотрудники")
Update(11)
Dele(4)