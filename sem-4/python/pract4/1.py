import inspect


# 1 задача. вывод атрибутов, кроме служебных
class MyClass:
    def __init__(self):
        self.field1 = 1
        self.field2 = "example"
        self._field2 = "hidden"

    def method1(self):
        return "Method 1 called"


obj = MyClass()
attrs = [attr for attr in dir(obj) if not inspect.ismethod(getattr(obj, attr))
         and not attr.startswith('_')]
print(attrs)


# 2 задача. Вызвать функцию по заданному названию

method_name = "method1"
if hasattr(obj, method_name):
    method = getattr(obj, method_name)
    result = method()
    print(result)
else:
    print(f"Метод с именем {method_name} не найден в классе MyClass.")

# 3 задача. В чем проблема?
"""
class A:
    pass

class B(A):
    pass

class C(A, B):
    pass
"""
# Ans: не нужно наследовать в С А, т.к. оно уже наследовано в B

# 4 задача. Однострочник для вывода иерархии наследования


get_inheritance = lambda cls: cls.__name__ + " -> ".join([c.__name__ for c in cls.__mro__[:]])

print(get_inheritance(OSError))
