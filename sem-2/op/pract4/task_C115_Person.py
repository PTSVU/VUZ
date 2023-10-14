import traceback
class Person:
    def __init__(self, name, surname, age):
        # Обработка исключений в конструкторе класса
        try:
            assert isinstance(name, str)
            assert isinstance(surname, str)
            assert isinstance(age, int)
        except:
            print("Error in Person")
        else:
            self.name = name
            self.surname = surname
            self.age = age


# Тесты
try:
    a = Person("Женя", "Норанов", 18)
    assert a.name == "Женя"
    assert a.surname == "Норанов"
    assert a.age == 18
except AssertionError:
    print("TEST Person ERROR")
    traceback.print_exc()
else:
    print("TEST Person PASSED")