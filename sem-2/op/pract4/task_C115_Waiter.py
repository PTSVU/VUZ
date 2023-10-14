from task_C115_Person import *

class Waiter(Person):
    def __init__(self, name, surname, age, checks):
        # Обработка исключений в конструкторе класса
        try:
            assert isinstance(name, str)
            assert isinstance(surname, str)
            assert isinstance(age, int)
            assert isinstance(checks, dict)
        except:
            print("Error in Waiter")
        else:
            super().__init__(name, surname, age)
            self.checks = checks

    def add_check(self, table_number, total_amount):
        # Метод добавления чека для указанного номера стола с указанной суммой
        self.checks[table_number] = total_amount
        # Присваивание элементу словаря checks с ключом table_number значения total_amount

    def remove_check(self, table_number):
        # Метод удаления чека для указанного номера стола
        del self.checks[table_number]
        # Удаление элемента словаря checks с ключом table_number

    def print_all_checks(self):
        # Метод вывода всех чеков
        for table_number, total_amount in self.checks.items():
            # Цикл for, проходящий по парам ключ-значение в словаре checks
            print(f"Стол {table_number}: {total_amount} руб.")
            # Вывод информации о номере стола и сумме чека

    def __str__(self):
        # Переопределение метода преобразования объекта класса в строку
        return f"\tИмя: {self.surname} {self.name} \n\tВозраст: {self.age}"
        # Возвращается строка с информацией об имени, фамилии и возрасте объекта класса



# Тесты
try:
    a = Waiter("Женя", "Норанов", 18, {"7": "1150р"})
    assert a.checks == {'7': '1150р'}
    a.__str__()
    a.add_check("1", "200")
    assert a.checks == {'7': '1150р', '1': '200'}
    a.remove_check("1")
    assert a.checks == {'7': '1150р'}
except AssertionError:
    print("TEST Waiter ERROR")
    traceback.print_exc()
else:
    print("TEST Waiter PASSED")