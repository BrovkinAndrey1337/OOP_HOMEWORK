import pytest

from src.product import Product


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
