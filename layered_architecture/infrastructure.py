import enum
from dataclasses import dataclass


# 食材の種別
class FoodType(enum.Enum):
    seasoning = "seasoning"
    ingredient = "ingredient"


# 食材データのデータ構造
@dataclass()
class FoodData:
    name: str
    calorie: int
    type: FoodType


class Infrastructure:
    @staticmethod
    def get_onion() -> FoodData:
        data = {"food_name": "onion", "food_calorie": 20}
        return FoodData(
            name=data["food_name"],
            calorie=data["food_calorie"],
            type=FoodType.ingredient,
        )

    @staticmethod
    def get_potato() -> FoodData:
        data = {
            "food_name": "potato",
            "food_calorie": 30,
        }
        return FoodData(
            name=data["food_name"],
            calorie=data["food_calorie"],
            type=FoodType.ingredient,
        )

    @staticmethod
    def get_carrot() -> FoodData:
        data = {
            "food_name": "carrot",
            "food_calorie": 40,
        }
        return FoodData(
            name=data["food_name"],
            calorie=data["food_calorie"],
            type=FoodType.ingredient,
        )

    @staticmethod
    def get_chicken() -> FoodData:
        data = {
            "food_name": "chicken",
            "food_calorie": 100,
        }
        return FoodData(
            name=data["food_name"],
            calorie=data["food_calorie"],
            type=FoodType.ingredient,
        )

    @staticmethod
    def get_curry_powder() -> FoodData:
        data = {
            "food_name": "curry_powder",
            "food_calorie": 20,
        }
        return FoodData(
            name=data["food_name"],
            calorie=data["food_calorie"],
            type=FoodType.seasoning,
        )

    @staticmethod
    def get_soy_sauce() -> FoodData:
        data = {
            "food_name": "soy_sauce",
            "food_calorie": 25,
        }
        return FoodData(
            name=data["food_name"],
            calorie=data["food_calorie"],
            type=FoodType.seasoning,
        )

    @staticmethod
    def get_sake() -> FoodData:
        data = {"food_name": "sake", "food_calorie": 40}
        return FoodData(
            name=data["food_name"],
            calorie=data["food_calorie"],
            type=FoodType.seasoning,
        )
