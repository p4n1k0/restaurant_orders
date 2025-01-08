from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient('carne')
    ingredient_2 = Ingredient('farinha')
    
    assert ingredient_1 is ingredient_1
    assert ingredient_1 != ingredient_2
    assert hash(ingredient_1) == hash(ingredient_1.name)
    assert str(ingredient_1) == f"Ingredient('{ingredient_1.name}')"
    assert ingredient_1.restrictions != set()
    assert ingredient_1.name == 'carne'
    assert ingredient_1 == ingredient_1
    assert ingredient_1 != ingredient_2
