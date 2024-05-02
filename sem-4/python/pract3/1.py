# 1.1
"""
module1.py
import module2

def func_module1():
    return module2.func_module2()

module2.py
import module1

def func_module2():
    return module1.func_module1()

При попытке вызова функции func из любого из модулей будет получена ошибка
"AttributeError: partially initialized module '...' has no attribute '...' (most likely due to a circular import)".
"""
# 1.2
"""
Модуль загружается только один раз при первом импорте.
При последующих импортах модуль будет использоваться из уже загруженного кэша.
"""
# 1.3
"""
from some_module import GLOBAL_VAR
GLOBAL_VAR = 42
приведет к изменению переменной только в данном модуле
1) изменить в каждом модуле some_module.GLOBAL_VAR = 42
2) Завести функцию, меняющее значение глобальной перемнной
"""
# 1.4
"""
# my_module.py
def func1():
    pass

def func2():
    pass

def func3():
    pass

__all__ = ['func1', 'func2']


from my_module import * - заимпортит только 2 функции
"""
# 1.5
"""
def load_config(filename):
    config = {}
    with open(filename, 'r') as file:
        config_script = file.read()
        exec(config_script, {}, config)
    return config
    
+
Безопасно
Удобство. Можно отследить все элементы конфигурации
-
Более сложный метод
Изменение в конфигурации может повлиять на другие модули
"""
# 1.6
"""
- Создали все файлы в директиве, написали логику
- Создаем setup.py
from setuptools import setup, find_packages

setup(
    name='my_education_package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
)
- Упаковка пакет
python setup.py sdist
- Установка виртуального окружения
python -m venv my_env создаем виртуалку
source my_env/bin/activate активируем
pip install my_education_package-1.0.0.tar.gz устанавливаем пакет
"""