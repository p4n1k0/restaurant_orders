from src.models.dish import Dish
from src.models.ingredient import Ingredient
from typing import Dict
import csv

Dishes = Dict[Dish, Dish]

# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        dishes_dict: Dishes = {}
        with open(source_path) as file:
            rows = csv.DictReader(file)
            for row in rows:
                dish_name = row['dish']
                if dish_name not in dishes_dict:
                    dishes_dict[dish_name] = Dish(
                        dish_name,
                        float(row['price'])
                    )
                dishes_dict[dish_name].add_ingredient_dependency(
                    Ingredient(row['ingredient']),
                    int(row['recipe_amount'])
                )
        self.dishes = set(dishes_dict.values())
