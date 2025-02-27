from typing import Any, Dict, List


class Product:
    """Класс продуктов"""

    _products: List["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product._products.append(self)

    def __str__(self):
        """Возвращает строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает стоимость двух продуктов с учетом их количества"""
        if not isinstance(other, Product):
            raise TypeError("Добавляемый объект должен быть экземпляром класса Product")
        total_value = (self.price * self.quantity) + (other.price * other.quantity)
        return total_value

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]):
        """Создает новый продукт или обновляет существующий"""
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        if name is None or description is None or price is None or quantity is None:
            raise ValueError("Все поля должны быть заполнены")

        for existing_product in cls._products:
            if existing_product.name == name:
                existing_product.quantity += quantity
                existing_product.__price = max(existing_product.__price, price)
                return existing_product

        new_product = cls(name, description, price, quantity)
        return new_product

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
