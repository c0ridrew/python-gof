import enum
from dataclasses import dataclass


# 料理データ
class FoodType(enum.Enum):
    seasoning = "seasoning"
    ingredient = "ingredient"


@dataclass()
class FoodData:
    food_name: str
    food_calorie: int
    food_type: str


def get_onion() -> FoodData:
    raw_data = {"food_name": "onion", "food_calorie": 20, "food_type": "ingredient"}
    return FoodData(**raw_data)


def get_potato() -> FoodData:
    raw_data = {"food_name": "potato", "food_calorie": 30, "food_type": "ingredient"}
    return FoodData(**raw_data)


def get_carrot() -> FoodData:
    raw_data = {"food_name": "carrot", "food_calorie": 40, "food_type": "ingredient"}
    return FoodData(**raw_data)


def get_curry_powder() -> FoodData:
    raw_data = {
        "food_name": "curry_powder",
        "food_calorie": 20,
        "food_type": "seasoning",
    }
    return FoodData(**raw_data)


def get_soy_sauce() -> FoodData:
    raw_data = {"food_name": "soy_sauce", "food_calorie": 25, "food_type": "seasoning"}
    return FoodData(**raw_data)


def get_sake() -> FoodData:
    raw_data = {"food_name": "sake", "food_calorie": 40, "food_type": "seasoning"}
    return FoodData(**raw_data)
