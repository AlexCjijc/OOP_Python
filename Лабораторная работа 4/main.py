class Device:
    """
    Базовый класс Device, представляющий электронное устройство.
    """

    def __init__(self, manufacturer: str, country_manufacturer: str, model: str) -> None:
        """
        Инициализация устройства с указанием производителя и модели.

        :param manufacturer: Название производителя устройства.
        :param country_manufacturer: Страна производителя устройства.
        :param model: Модель устройства.
        """
        self._manufacturer = manufacturer  # инкапсуляция: производитель является внутренним свойством
        self.country_manufacturer = country_manufacturer
        self.model = model

    def __str__(self) -> str:
        """
        Строковое представление устройства.
        """
        return f"{self._manufacturer} {self.country_manufacturer} {self.model}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта.
        """
        return f"Device(manufacturer='{self._manufacturer}'," \
               f"country_manufacturer= '{self.country_manufacturer}', model='{self.model}')"

    def get_info(self) -> str:
        """
        Возвращает информацию об устройстве.
        """
        return f"устройство компании {self._manufacturer} и модель это {self.model}"

    def get_country(self) -> str:
        """
        Возвращает страну производства.
        """
        return f"Это устройство производства {self.country_manufacturer}"


class Smartphone(Device):
    """
    Класс Smartphone является дочерним классом класса Device
    """

    def __init__(self, manufacturer: str, country_manufacturer: str, model: str, os: str) -> None:
        """
        Инициализация смартфона с операционной системой в дополнение к производителю и модели.

        :param manufacturer: Название производителя смартфона.
        :param model: Модель смартфона.
        :param os: Операционная система смартфона.
        """
        super().__init__(manufacturer, country_manufacturer, model)  # вызываем конструктор базового класса
        self.os = os  # новый атрибут для класса Smartphone

    def __repr__(self) -> str:
        """
        Перегрузка метода.
        Официальное строковое представление объекта.
        """
        return f"Smartphone(manufacturer='{self._manufacturer}', " \
               f"country_manufacturer= '{self.country_manufacturer}', model='{self.model}', OS='{self.os}')"

    def get_info(self) -> str:
        """
        Перегружаем метод для получения расширенной информации о смартфоне,
        тк добавляем данные об операционной системе.
        """
        base_info = super().get_info()  # вызываем метод базового класса
        return f"Информация о смартфоне: {base_info}, работает на операционной системе {self.os}"

    def make_call(self, number: str) -> str:
        """
        Инструкция для смартфона сделать вызов по указанному номеру.

        :param number: Номер телефона.
        """
        return f"Смартфон {self.model} набирает номер {number} и осуществляет вызов."

    def send_sms(self, number: str, message: str) -> str:
        """
        Отправка SMS-сообщения смартфоном на указанный номер.

        :param number: Номер телефона.
        :param message: Текст сообщения.
        """
        return f"Смартфон {self.model} отправляет SMS-сообщение на номер {number}: {message}"


class Laptop(Device):
    """
    Класс Laptop является дочерним классом класса Device
    """

    def __init__(self, manufacturer: str, country_manufacturer: str, model: str, os: str) -> None:
        """
        Инициализация смартфона с операционной системой в дополнение к производителю и модели.

        :param manufacturer: Название производителя ноутбука.
        :param model: Модель ноутбука.
        :param os: Операционная система ноутбука.
        """
        super().__init__(manufacturer, country_manufacturer, model)  # вызываем конструктор базового класса
        self.os = os  # новый атрибут для класса Laptop

    def __repr__(self) -> str:
        """
        Перегрузка метода.
        Официальное строковое представление объекта.
        """
        return f"Laptop(manufacturer='{self._manufacturer}', " \
               f"country_manufacturer= '{self.country_manufacturer}', model='{self.model}', OS='{self.os}')"

    def get_info(self) -> str:
        """
        Перегружаем метод для получения расширенной информации о ноутбуке,
        тк добавляем данные об операционной системе.
        """
        base_info = super().get_info()  # вызываем метод базового класса
        return f"Информация о ноутбуке: {base_info}, работает на операционной системе {self.os}"

    def power_on(self) -> str:
        """
        Включение ноутбука.

        """
        return f"Ноутбук {self.model} включается."

    def power_off(self) -> str:
        """
        Выключение ноутбука.

        """
        return f"Ноутбук {self.model} выключается."


if __name__ == "__main__":
    smartphone = Smartphone("CoolBrand", "Япония", "ModelY", "Android")
    print(smartphone)
    print(repr(smartphone))
    print(smartphone.get_country())    # использование наследуемого метода
    print(smartphone.get_info())  # использование перегруженного метода
    print(smartphone.make_call("+79130010011"))
    print(smartphone.send_sms("+79130010011", "Привет, как дела?"))

    print("-" * 40)

    laptop = Laptop("Lenovik", "Китай", "Idolpad", "Windows")
    print(laptop)
    print(repr(laptop))
    print(laptop.get_country())    # использование наследуемого метода
    print(laptop.get_info())  # использование перегруженного метода
    print(laptop.power_on())
    print(laptop.power_off())
pass
