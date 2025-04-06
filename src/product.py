from typing import Any, Dict, List

from src.BaseProduct import BaseProduct
from src.MixinInfo import MixinInfo


class Product(MixinInfo, BaseProduct):
    """Класс продуктов"""

    _products: List["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)
        Product._products.append(self)

    def __repr__(self):
        """Возвращает строковое представление продукта"""
        return f"{self.__class__.__name__}: {self.name}, {self.description}, {self.price}, {self.quantity}"

    def __str__(self):
        """Возвращает строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает стоимость двух продуктов с учетом их количества"""
        if not isinstance(other, BaseProduct):
            raise TypeError(
                "Добавляемый объект должен быть экземпляром класса BaseProduct"
            )
        if not isinstance(other, type(self)):
            raise TypeError("Нельзя складывать продукты разных классов")
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
                existing_product.price = max(existing_product.price, price)
                return existing_product

        new_product = cls(name, description, price, quantity)
        return new_product
