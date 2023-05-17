from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    with pytest.raises(TypeError, match='Dish price must be float.'):
        Dish('', 'Invalid price type')
    with pytest.raises(ValueError, match='Dish price must be greater then zero.'):
        Dish('', 0)

    dish = Dish('Home dish', 10.0)
    dish.add_ingredient_dependency('queijo mussarela', 1)
    dish2 = Dish('Travel dish', 20.0)

    assert dish.name == 'Home dish'
    assert dish.price == 10.0
    assert dish.recipe == {'queijo mussarela': 1}
    assert hash(dish) == hash("Dish('Home dish', R$10.00)")
    assert dish == dish
    assert dish != dish2
    assert dish.get_ingredients() == {'queijo mussarela'}
    assert dish2.get_restrictions() == set()
    assert dish.get_ingredients() == {'queijo mussarela'}
