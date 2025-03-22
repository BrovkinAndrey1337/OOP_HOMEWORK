from src.product import Product


class LawnGrass(Product):
    """Класс газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Возвращает строковое представление газонной травы"""
        return (
            f"{super().__str__()}, Страна-производитель: {self.country}, "
            f"Срок прорастания: {self.germination_period} дней, Цвет: {self.color}"
        )
