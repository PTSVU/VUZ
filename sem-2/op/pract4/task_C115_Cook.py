from task_C115_Waiter import *

class Cook(Person):
    def __init__(self, name, surname, age, specialty, dishes):
        # Обработка исключений в конструкторе класса
        try:
            assert isinstance(name, str)
            assert isinstance(surname, str)
            assert isinstance(age, int)
            assert isinstance(specialty, str)
            assert isinstance(dishes, dict)
        except:
            print("Error in Cook")
        else:
            super().__init__(name, surname, age)
            self.specialty = specialty
            self.dishes = dishes

    def change_specialty(self, new_specialty):
        # Метод изменения специальности повара на новую специальность
        self.specialty = new_specialty
        # Присваивание атрибуту specialty нового значения new_specialty

    def add_dish(self, dish_name, preparation_time):
        # Метод добавления блюда с указанным названием и временем приготовления
        self.dishes[dish_name] = preparation_time
        # Добавление элемента в словарь dishes с ключом dish_name и значением preparation_time

    def remove_dish(self, dish_name):
        # Метод удаления блюда с указанным названием
        if dish_name in self.dishes:
            # Проверка, содержится ли блюдо с указанным названием в словаре dishes
            del self.dishes[dish_name]
            # Удаление элемента из словаря dishes с ключом dish_name

    def get_dish_list(self):
        # Метод вывода списка всех блюд и времени их приготовления
        for dish, time in self.dishes.items():
            # Цикл for, проходящий по парам ключ-значение в словаре dishes
            print(f"Блюдо {dish}, время его приготовления {time}")
            # Вывод информации о блюде и времени его приготовления

    def __str__(self):
        # Переопределение метода объекта класса в строку
        return f"\tИмя: {self.surname} {self.name} \n\tВозраст: {self.age} \n\tСпециальность: {self.specialty}"
        # Возвращается строка с информацией об имени, фамилии, возрасте и специальности повара


# Тесты
try:
    a = Cook("Женя", "Норанов", 18, "Повар", {"Суп": "1ч"})
    assert a.specialty == "Повар"
    assert a.dishes == {'Суп': '1ч'}
    a.__str__()
    a.change_specialty("Шеф повар")
    assert a.specialty == "Шеф повар"
    a.add_dish("Макароны", "30м")
    assert a.dishes == {'Суп': '1ч', 'Макароны': '30м'}
    a.remove_dish("Макароны")
    assert a.dishes == {'Суп': '1ч'}
except AssertionError:
    print("TEST Cook ERROR")
    traceback.print_exc()
else:
    print("TEST Cook PASSED")