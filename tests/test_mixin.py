import pytest
from src.product import Product
from src.LawnGrass import LawnGrass
from src.smartphone import Smartphone


def test_mixin_info_repr_LawnGrass():
    grass = LawnGrass("Трава", "Газонная трава", 1000, 5, "США", 14, "Зеленая")
    expected_grass_repr = "LawnGrass: Трава, Газонная трава, 1000, 5, США, 14, Зеленая"
    assert repr(grass) == expected_grass_repr


def test_mixin_info_repr_Product():
    product = Product("Товар", "Описание товара", 500, 10)
    expected_product_repr = "Product: Товар, Описание товара, 500, 10"
    assert repr(product) == expected_product_repr


def test_mixin_info_repr_Smartphone():
    smartphone = Smartphone(
        "Смартфон XYZ",
        "Современный смартфон",
        25000,
        5,
        "Высокая",
        "Model 1",
        128,
        "Черный",
    )
    expected_smartphone_repr = "Smartphone: Смартфон XYZ, Современный смартфон, 25000, 5, Высокая, Model 1, 128, Черный"
    assert repr(smartphone) == expected_smartphone_repr
