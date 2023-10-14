from task_C115_Cook import *

class Cafe:
    def __init__(self, name, address, waiters, cooks):
        # Обработка исключений в конструкторе класса
        try:
            assert isinstance(name, str)
            assert isinstance(address, str)
            assert isinstance(waiters, list)
            assert isinstance(cooks, list)
        except:
            print("Error in Cafe")
        else:
            self.name = name
            self.address = address
            self.waiters = waiters
            self.cooks = cooks

    def __str__(self):
        # Переопределение метода преобразования объекта класса в строку
        print(f"\tКафе: {self.name}\n\tАдрес: {self.address}")
        # Вывод информации о названии и адресе кафе
        print(f"\n\tОфицианты:")
        # Вывод заголовка для списка официантов
        print([self.waiters[i].__str__() for i in range(len(self.waiters))])
        # Вывод информации о каждом официанте в списке официантов
        print(f"\n\tПовара:")
        # Вывод заголовка для списка поваров
        print([self.cooks[i].__str__() for i in range(len(self.cooks))])
        # Вывод информации о каждом поваре в списке поваров

    def __len__(self):
        # Метод возвращает общее количество работников (официантов и поваров)
        return len(self.waiters) + len(self.cooks)

    def __getitem__(self, index):
        # Метод получения элемента по индексу
        if index < len(self.waiters):
            # Если индекс находится в пределах списка официантов
            return self.waiters[index]
            # Возвращается официант по указанному индексу
        elif index < len(self.waiters) + len(self.cooks):
            # Если индекс находится в пределах списка поваров
            return self.cooks[index - len(self.waiters)]
            # Возвращается повар по указанному индексу
        else:
            print("Индекс выходит за пределы")

    def __setitem__(self, index, value):
        # Метод установки значения элемента по индексу
        if index < len(self.waiters):
            # Если индекс находится в пределах списка официантов
            self.waiters[index] = value
            # Устанавливается новое значение официанта по указанному индексу
        elif index < len(self.waiters) + len(self.cooks):
            # Если индекс находится в пределах списка поваров
            self.cooks[index - len(self.waiters)] = value
            # Устанавливается новое значение повара по указанному индексу
        else:
            print("Индекс выходит за пределы")

    def __delitem__(self, index):
        # Метод удаления элемента по индексу
        if index < len(self.waiters):
            # Если индекс находится в пределах списка официантов
            del self.waiters[index]
            # Удаляется официант по указанному индексу
        elif index < len(self.waiters) + len(self.cooks):
            # Если индекс находится в пределах списка поваров
            del self.cooks[index - len(self.waiters)]
            # Удаляется повар по указанному индексу
        else:
            print("Индекс выходит за пределы")

    def __add__(self, worker):
        # Метод добавления работника
        if isinstance(worker, Waiter):
            # Если работник является официантом
            self.waiters.append(worker)
            # Официант добавляется в список официантов
        elif isinstance(worker, Cook):
            # Если работник является поваром
            self.cooks.append(worker)
            # Повар добавляется в список поваров
        else:
            print("Недопустимый тип работника")
    def __sub__(self, worker):
        # Метод удаления работника
        if isinstance(worker, Waiter):
            # Если работник является официантом
            for i in range(len(self.waiters)):
                # Цикл по всем официантам в списке официантов
                if self.waiters[i] == worker:
                    del self.waiters[i]
                    # Если официант найден, он удаляется из списка официантов
                elif i == len(self.waiters):
                    print("Такой работник отсутствует")
                    # Если прошли по всем официантам и не нашли совпадений, выводится сообщение
        elif isinstance(worker, Cook):
            # Если работник является поваром
            for i in range(len(self.cooks)):
                # Цикл по всем поварам в списке поваров
                if self.cooks[i] == worker:
                    del self.cooks[i]
                    # Если повар найден, он удаляется из списка поваров
                elif i == len(self.cooks):
                    print("Такой работник отсутствует")
                    # Если прошли по всем поваром и не нашли совпадений, выводится сообщение
        elif isinstance(worker, str):
            # Если работник передан в виде строки (имени работника)
            for i in range(self.__len__()):
                # Цикл по всем работникам
                try:
                    if i < len(self.waiters) and self.waiters[i].name == worker:
                        del self.waiters[i]
                        # Если работник с указанным именем является официантом, он удаляется из списка официантов
                    elif (i < len(self.waiters) + len(self.cooks)) and self.cooks[i - len(self.waiters)].name == worker:
                        del self.cooks[i - len(self.waiters)]
                        # Если работник с указанным именем является поваром, он удаляется из списка поваров
                except IndexError:
                    print("Работник с таким именем отсутствует")
                    # Если прошли по всем работникам и не нашли совпадений, выводится сообщение
        else:
            print("Недопустимый тип работника")

    def create_info_file(self):
        # Метод создания информационного файла о кафе
        with open("task_С115_Cafe.txt", "w") as file:
            file.write(f"Кафе: {self.name}\nАдрес: {self.address}\n\nОфицианты:\n")
            # Запись названия кафе и адреса в файл
            for waiter in self.waiters:
                file.write(str(waiter) + "\n")
                # Запись информации об официантах в файл
            file.write("\nПовара:\n")
            # Заголовок для списка поваров в файле
            for cook in self.cooks:
                file.write(str(cook) + "\n")
                # Запись информации о поварах в файл



# Тесты
try:
    waiter = [Waiter("Витя", "Альварес", 18, {"7": "1150р"}), Waiter("Коля", "Альварес", 19, {"1": "370р"})]
    cook = [Cook("Женя", "Норанов", 21, "Повар", {"Суп": "1ч"}), Cook("Саша", "Норанов", 25, "Шеф повар", {"Макароны": "30м"})]
    a = Cafe("Алфат", "пр.Вернадского 78", waiter, cook)
    assert len(a) == 4
    a.__getitem__(1)
    a.__setitem__(1, Waiter("Вова", "Альварес", 20, {"13": "1770р"}))
    a.__delitem__(1)
    a.__add__(Waiter("Коля", "Альварес", 19, {"8": "3270р"}))
    a.__sub__(Waiter("Коля", "Альварес", 19, {"8": "3270р"}))
    a.__sub__("Женя")
    a.create_info_file()
except AssertionError:
    print("TEST Cafe ERROR")
    traceback.print_exc()
else:
    print("TEST Cafe PASSED")