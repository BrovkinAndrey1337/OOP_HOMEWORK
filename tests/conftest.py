import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    return Product(
        name="Товар 1", description="Описание товара 1", price=100.0, quantity=10
    )


@pytest.fixture
def sample_category(sample_product):
    return Category(
        name="Категория 1",
        description="Описание категории 1",
        products=[sample_product],
    )
