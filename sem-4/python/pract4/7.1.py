import inspect
import importlib.util

def generate_documentation(module_name):
    try:
        spec = importlib.util.spec_from_file_location(module_name, module_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        print(f"# Модуль {module_name}\n")
        print(inspect.getdoc(module))

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                print(f"\n## Класс {name}\n")
                print(inspect.getdoc(obj))
                for attr_name, attr in inspect.getmembers(obj):
                    if inspect.isfunction(attr) or inspect.ismethod(attr):
                        print(f"* **Метод** `{attr_name}{inspect.signature(attr)}`")
                        print(inspect.getdoc(attr))
            elif inspect.isfunction(obj):
                print(f"\n## Функция {name}\n")
                print(f"Сигнатура: `{name}{inspect.signature(obj)}`")
                print(inspect.getdoc(obj))

    except Exception as e:
        print(f"Ошибка при генерации документации для модуля {module_name}: {e}")

# Пример использования
generate_documentation("7.py")
