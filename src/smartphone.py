from src.product import Product


class Smartphone(Product):
    """Класс смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        """Возвращает строковое представление продукта"""
        return f"{self.__class__.__name__}: {self.name}, {self.description}, {self.price}, {self.quantity}, {self.efficiency}, {self.model}, {self.memory}, {self.color}"

    def __str__(self):
        """Возвращает строковое представление смартфона"""
        return (
            f"{super().__str__()}, Модель: {self.model}, "
            f"Эффективность: {self.efficiency}, "
            f"Память: {self.memory} ГБ, Цвет: {self.color}"
        )
