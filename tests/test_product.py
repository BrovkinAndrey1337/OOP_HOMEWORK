import pytest

from src.product import Product
from src.smartphone import Smartphone
from src.LawnGrass import LawnGrass


def test_product_initialization(sample_product):
    assert sample_product.name == "Товар 1"
    assert sample_product.description == "Описание товара 1"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_new_product_creation():
    product_data = {
        "name": "Товар 4",
        "description": "Описание товара 2",
        "price": 200.0,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    assert product.name == "Товар 4"
    assert product.price == 200.0
    assert product.quantity == 5


def test_update_existing_product(sample_product):
    product_data = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 150.0,
        "quantity": 5,
    }
    updated_product = Product.new_product(product_data)
    assert updated_product.quantity == 15
    assert updated_product.price == 150.0


def test_product_creation_with_missing_fields():
    product_data = {
        "name": None,
        "description": "Описание товара 3",
        "price": 300.0,
        "quantity": 5,
    }
    with pytest.raises(ValueError, match="Все поля должны быть заполнены"):
        Product.new_product(product_data)


def test_price_setter(sample_product):
    sample_product.price = 120.0
    assert sample_product.price == 120.0


def test_price_setter_lower_price(sample_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "y")
    sample_product.price = 80.0
    assert sample_product.price == 80.0


def test_price_setter_negative_price(sample_product):
    sample_product.price = -50.0
    assert sample_product.price == 100.0


def test_add_products(sample_product, another_product):
    total_price = sample_product + another_product
    assert total_price == 1750.0


def test_str_method(sample_product):
    expected_str = "Товар 1, 100.0 руб. Остаток: 10 шт."
    assert str(sample_product) == expected_str


def test_smartphone_creation():
    smartphone = Smartphone(
        name="iPhone",
        description="Смартфон от Apple",
        price=999.99,
        quantity=5,
        efficiency="Высокая",
        model="iPhone 14",
        memory=128,
        color="Черный",
    )

    assert smartphone.name == "iPhone"
    assert smartphone.description == "Смартфон от Apple"
    assert smartphone.price == 999.99
    assert smartphone.quantity == 5
    assert smartphone.efficiency == "Высокая"
    assert smartphone.model == "iPhone 14"
    assert smartphone.memory == 128
    assert smartphone.color == "Черный"
    assert str(smartphone) == (
        "iPhone, 999.99 руб. Остаток: 5 шт., Модель: iPhone 14, "
        "Эффективность: Высокая, Память: 128 ГБ, Цвет: Черный"
    )


def test_lawn_grass_creation():
    lawn_grass = LawnGrass(
        name="Газонная трава",
        description="Трава для газонов",
        price=50.0,
        quantity=100,
        country="Россия",
        germination_period=14,
        color="Зеленый",
    )

    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Трава для газонов"
    assert lawn_grass.price == 50.0
    assert lawn_grass.quantity == 100
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 14
    assert lawn_grass.color == "Зеленый"
    assert str(lawn_grass) == (
        "Газонная трава, 50.0 руб. Остаток: 100 шт., "
        "Страна-производитель: Россия, Срок прорастания: 14 дней, Цвет: Зеленый"
    )


def test_product_addition_different_classes():
    """Тестирование сложения продуктов разных классов"""
    product1 = Smartphone(
        name="iPhone",
        description="Смартфон от Apple",
        price=999.99,
        quantity=1,
        efficiency="Высокая",
        model="iPhone 14",
        memory=128,
        color="Черный",
    )
    product2 = LawnGrass(
        name="Газонная трава",
        description="Трава для газонов",
        price=50.0,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="Зеленый",
    )

    with pytest.raises(TypeError, match="Нельзя складывать продукты разных классов"):
        product1 + product2


def test_product_addition_invalid_type():
    """Тестирование сложения с объектом неправильного типа"""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=1)

    with pytest.raises(
        TypeError, match="Добавляемый объект должен быть экземпляром класса BaseProduct"
    ):
        product + "не продукт"

def test_product_init_invalid_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Товар 2", "Описание товара 2", 50.0, 0)