from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для установки цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                print("Вы согласны понизить цену? y - да")
                answer = input()
                if answer.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price

    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление продукта"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Складывает стоимость двух продуктов с учетом их количества"""
        pass

    @abstractmethod
    def __repr__(self):
        """Возвращает строковое представление продукта"""
        pass
