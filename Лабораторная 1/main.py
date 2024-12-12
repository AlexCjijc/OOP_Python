import doctest
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов

class Tree:
    def __init__(self, name: str, age: int, current_height:  Union[int, float]):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param name: Наименование дерева
        :param age: Возраст дерева
        :param current_height: Текущая высота дерева

        Примеры:
        >>> tree1 = Tree("Oak", 9, 5.5)  # инициализация экземпляра класса
        >>> tree2 = Tree("Pine", 40, 14)
        """
        self.name = name
        self.age = age
        self.current_height = current_height

        if not isinstance(name, str):
            raise TypeError("Наименование дерева должно быть типа str")
        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типа int")
        if not isinstance(current_height, (int, float)):
            raise TypeError("Текущая высота дерева должна быть типа int или float")

        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        if current_height < 0:
            raise ValueError("Текущая высота дерева не может быть отрицательным числом")

    def tree_growth(self, growth_height: Union[int, float]) -> None:
        """
        Приорост дерева
        :param growth_height: Высота прироста дерева

        :raise ValueError: Если высота приороста дерева не положительно число, то вызываем ошибку

        Примеры:
        >>> tree1 = Tree("Oak", 9, 5.5)
        >>> tree1.tree_growth(1.2)
        """
        if not isinstance(growth_height, (int, float)):
            raise TypeError("Высота прироста дерева должна быть типа int или float")
        if growth_height <= 0:
            raise ValueError("Высота прироста дерева должна положительным числом")
        ...
    def add_years(self, years: int) -> None:
        """
        Добавление лет к возрасту дерева
        :param years: Добавляемые года к возрасту дерева

        :raise ValueError: Если добавляемые года к возрасту дерева не положительно число, то вызываем ошибку

        Примеры:
        >>> tree1 = Tree("Oak", 9, 5.5)
        >>> tree1.add_years(2)
        """
        if not isinstance(years, int):
            raise TypeError("Добавляемые года к возрасту дерева должны быть типа int")
        if years <= 0:
            raise ValueError("Добавляемые года к возрасту дерева должны быть положительным числом")
        ...
    def tree_cutting(self, tree_cutting_height:  Union[int, float]) -> None:
        """
        Обрезка дерева
        :param tree_cutting_height: Высота обрезки дерева

        :raise ValueError: Если высота обрезки дерева не положительно число, то вызываем ошибку

        Примеры:
        >>> tree1 = Tree("Oak", 9, 5.5)
        >>> tree1.tree_cutting(0.5)
        """
        if not isinstance(tree_cutting_height, (int, float)):
            raise TypeError("Высота обрезки дерева должна быть типа int или float")
        if tree_cutting_height <= 0:
            raise ValueError("Высота обрезки дерева должна быть типа положительным числом")
        ...

class Table:
    def __init__(self,  material: str, objects: list, height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола
        :param objects: Объекты размещенные на столе
        :param height: Высота стола

        Примеры:
        >>> table = Table("Oak", ["cup", "laptop"], 0.8)  # инициализация экземпляра класса

        """
        self.material = material
        self.objects = objects
        self.height = height

        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        if not isinstance(objects, list):
            raise TypeError("Объекты на столе должны быть типа list")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть типа int или float")

        if height < 0:
            raise ValueError("Высота стола не может быть отрицательным числом")

    def add_object_on_table(self, added_object: str) -> None:
        """
        Добавление объектов на стол
        :param added_object: добавлямый объект

        :raise ValueError: Если добавляемый объект пустой, то вызываем ошибку

        Примеры:
        >>> table = Table("Oak", ["cup", "laptop"], 0.8)
        >>> table.add_object_on_table("keyboard")
        """
        if not isinstance(added_object, str):
            raise TypeError("Добавлямый объект должен быть типа str")
        if added_object == "":
            raise ValueError("Добавлямый объект не может быть пустым")
        ...
    def is_empty_table(self) -> bool:
        """
        Функция, которая проверяет является ли стол пустым

        :return: Является ли стол пустым

        Примеры:
        >>> table = Table("Oak", ["cup", "laptop"], 0.8)
        >>> table.is_empty_table()
        """
        ...
    def clean_table(self) -> None:
        """
        Функция, которая очищает стол

        Примеры:
        >>> table = Table("Oak", ["cup", "laptop"], 0.8)
        >>> table.clean_table()
        """
        ...

class Social_network:
    def __init__(self, name:str, platform: list, users_online: int, version: float):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Наименование социальной сети
        :param platform: Поддерживаемые платофрмы
        :param users_online: Количество пользователей онлайн
        :param version: Версия

        Примеры:
        >>> vk = Social_network("Вконтакте", ["Android", "IOS"], 89180000, 8.59)  # инициализация экземпляра класса

        """
        if not isinstance(name, str):
            raise TypeError("Наименование социальной сети должно быть типа str")
        if not isinstance(platform, list):
            raise TypeError("Поддерживаемые платофрмы должны быть типа list")
        if not isinstance(users_online, int):
            raise TypeError("Количество пользователей онлайн должно быть типа int")
        if not isinstance(version, float):
            raise TypeError("Версия социальной сети должна быть типа float")


        if users_online < 0:
            raise ValueError("Количество пользователей онлайн не может быть отрицательным числом")
        if version < 0:
            raise ValueError("Версия социальной сети не может быть отрицательным числом")

    def is_empty_social_network(self) -> bool:
        """
        Функция, которая проверяет является ли социальная сеть пустым, то есть в ней
        нет пользователей в сети

        :return: Является ли социальная сеть пустым

        Примеры:
        >>> vk = Social_network("Вконтакте", ["Android", "IOS"], 89180000, 8.59)
        >>> vk.is_empty_social_network()
        """
        ...
    def update_version(self, current_version: float, new_version: float) -> None:
        """
        Обновление версии
        :param new_version: Новая версия социальной сети

        :raise ValueError: Если новая версия меньше по значению текущей версии, то вызываем ошибку

        Примеры:
        >>> vk = Social_network("Вконтакте", ["Android", "IOS"], 89180000, 8.59)
        >>> vk.update_version(8.59, 8.6)
        """
        if not isinstance(new_version, float):
            raise TypeError("Новая версия социальной сети должна быть типа float")
        if current_version > new_version:
            raise ValueError("Новая версия социальной сети должна быть выше по значению текущей версии")
        ...

    def add_platform(self, added_platform: str) -> None:
        """
        Добавление новой поддерживающей платформы
        :param added_platform: добавляемая плафторма

        :raise ValueError: Если добавляемая плафторма пустая, то вызываем ошибку

        Примеры:
        >>> vk = Social_network("Вконтакте", ["Android", "IOS"], 89180000, 8.59)
        >>> vk.add_platform("Linux")
        """
        if not isinstance(added_platform, str):
            raise TypeError("Добавляемая плафторма должна быть типа str")
        if added_platform == "":
            raise ValueError("Добавляемая плафторма не может быть пустым")
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
