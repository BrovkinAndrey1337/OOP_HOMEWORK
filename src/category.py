from typing import List

from src.product import Product


class Category:
    """Класс категорий продуктов"""

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию, проверяя его тип"""
        if not isinstance(product, Product):
            raise TypeError("Добавляемый объект должен быть экземпляром класса Product")
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        """Возвращает список продуктов в формате строки"""
        return "\n".join(str(product) for product in self.__products).strip()

