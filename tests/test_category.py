from src.category import Category
from src.product import Product
import pytest

def test_category_initialization(sample_category):
    assert sample_category.name == "Категория 1"
    assert sample_category.description == "Описание категории 1"
    assert len(sample_category.products.splitlines()) == 1
    assert Category.total_categories == 1
    assert Category.total_products == 1


def test_add_product(sample_category):
    initial_total_products = Category.total_products
    new_product = Product(
        name="Товар 2", description="Описание товара 2", price=200.0, quantity=5
    )
    sample_category.add_product(new_product)

    assert Category.total_categories == 2
    assert len(sample_category.products.splitlines()) == 2
    assert Category.total_products == initial_total_products + 1


def test_products_string_representation(sample_category):
    expected_output = "Товар 1, 100.0 руб. Остаток: 10 шт."
    assert sample_category.products == expected_output

def test_average_price_empty_category():
    category = Category("Продукты", "Описание", [])
    with pytest.raises(ValueError, match="В категории нет товаров для расчета средней цены."):
        category.average_price()


def test_average_price_with_products():
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)
    category = Category("Продукты", "Описание", [product1, product2])

    assert category.average_price() == (100.0 + 200.0) / 2