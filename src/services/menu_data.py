from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.load_menu_data(source_path)

    def load_menu(self, source_path: str) -> None:
        with open(source_path, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            dishes = {}
            for row in reader:
                (
                    dish_name,
                    dish_price,
                    ingredient_name,
                    ingredient_quantity
                ) = row
                dish = dishes.get(dish_name)
                if not dish:
                    dish = Dish(dish_name, float(dish_price))
                    dishes[dish_name] = dish
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(
                    ingredient,
                    int(ingredient_quantity)
                )
                self.ingredients.add(ingredient)
        self.dishes.update(dishes.values())
