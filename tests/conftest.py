import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_koumiss():
    product = Product("Кумыс", "Райское наслаждение", 13.37, 5)
    return product


@pytest.fixture
def product_beer():
    product = Product("Пиво", "Будущее будет светлым и нефильтрованным", 22.8, 1)
    return product


@pytest.fixture
def category_of_2_products(product_koumiss, product_beer):
    category1 = Category(
        "2 на выбор", "Выбирай любое, не ошибешься", [product_beer, product_koumiss]
    )
    category2 = Category("1 на выбор", "Возьми меня", [product_beer])
    return category1, category2
