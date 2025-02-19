from src.category import Category


def test_category_of_products(category_of_2_products):
    category1, category2 = category_of_2_products

    assert category1.name == "2 на выбор"
    assert category1.description == "Выбирай любое, не ошибешься"
    assert len(category1.products) == 2
    assert category1.products[0].name == "Пиво"
    assert category1.products[1].name == "Кумыс"

    assert category2.name == "1 на выбор"
    assert category2.description == "Возьми меня"
    assert len(category2.products) == 1
    assert category2.products[0].name == "Пиво"

    assert Category.total_categories == 2
