def test_product_koumiss(product_koumiss, product_beer):
    assert product_koumiss.name == "Кумыс"
    assert product_koumiss.description == "Райское наслаждение"
    assert product_koumiss.price == 13.37
    assert product_koumiss.quantity == 5
    assert product_beer.name == "Пиво"
    assert product_beer.description == "Будущее будет светлым и нефильтрованным"
    assert product_beer.price == 22.8
    assert product_beer.quantity == 1
