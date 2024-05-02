import os
import inspect
from graphviz import Digraph


def generate_module_documentation(module_name):
    module = __import__(module_name)
    doc = inspect.getdoc(module)
    classes = inspect.getmembers(module, inspect.isclass)
    functions = inspect.getmembers(module, inspect.isfunction)

    result = f"# Модуль {module_name}\n\n"
    if doc:
        result += f"{doc}\n\n"

    for class_name, class_object in classes:
        result += f"## Класс {class_name}\n\n"
        class_doc = inspect.getdoc(class_object)
        if class_doc:
            result += f"{class_doc}\n\n"

        methods = inspect.getmembers(class_object, inspect.ismethod)
        for method_name, method_object in methods:
            method_doc = inspect.getdoc(method_object)
            method_signature = inspect.signature(method_object)
            result += f"* **Метод** `{method_name}{method_signature}`\n\n"
            if method_doc:
                result += f"{method_doc}\n\n"

    for function_name, function_object in functions:
        result += f"## Функция {function_name}\n\n"
        function_doc = inspect.getdoc(function_object)
        function_signature = inspect.signature(function_object)
        if function_doc:
            result += f"Сигнатура: `{function_signature}`\n\n"
            result += f"{function_doc}\n\n"

    return result


def visualize_project_hierarchy(project_path):
    dot = Digraph()

    def add_modules_to_dot(directory, parent=None):
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)
            if os.path.isfile(full_path) and item.endswith('.py'):
                module_name = item[:-3]
                dot.node(module_name)
                if parent:
                    dot.edge(parent, module_name)
            elif os.path.isdir(full_path):
                subdir = os.path.join(directory, item)
                if parent:
                    dot.edge(parent, item)
                add_modules_to_dot(subdir, parent=item)

    add_modules_to_dot(project_path)
    dot.render('project_hierarchy', format='png', cleanup=True)


# Пример использования
module_documentation = generate_module_documentation('7')
print(module_documentation)

visualize_project_hierarchy('C:\\Users\\ptsvu\\Desktop\\rab\\cod\\PyCharm\\main')
