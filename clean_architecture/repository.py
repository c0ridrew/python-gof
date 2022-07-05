from clean_architecture.entity import Ingredient, Seasoning
from clean_architecture.i_repository import IRepository


class Repository(IRepository):
    @staticmethod
    def get_onion() -> Ingredient:
        data = {"food_name": "onion", "food_calorie": 20}
        return Ingredient(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_potato() -> Ingredient:
        data = {"food_name": "potato", "food_calorie": 30}
        return Ingredient(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_carrot() -> Ingredient:
        data = {"food_name": "carrot", "food_calorie": 40}
        return Ingredient(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_curry_powder() -> Seasoning:
        data = {"food_name": "curry_powder", "food_calorie": 20}
        return Seasoning(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_soy_sauce() -> Seasoning:
        data = {"food_name": "soy_sauce", "food_calorie": 25}
        return Seasoning(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_sake() -> Seasoning:
        data = {"food_name": "sake", "food_calorie": 40}
        return Seasoning(name=data["food_name"], calorie=data["food_calorie"])


class DevRepository(IRepository):
    @staticmethod
    def get_onion() -> Ingredient:
        data = {"food_name": "onion", "food_calorie": -20}
        return Ingredient(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_potato() -> Ingredient:
        data = {"food_name": "potato", "food_calorie": -30}
        return Ingredient(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_carrot() -> Ingredient:
        data = {"food_name": "carrot", "food_calorie": -40}
        return Ingredient(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_curry_powder() -> Seasoning:
        data = {"food_name": "curry_powder", "food_calorie": -20}
        return Seasoning(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_soy_sauce() -> Seasoning:
        data = {"food_name": "soy_sauce", "food_calorie": -25}
        return Seasoning(name=data["food_name"], calorie=data["food_calorie"])

    @staticmethod
    def get_sake() -> Seasoning:
        data = {"food_name": "sake", "food_calorie": -40}
        return Seasoning(name=data["food_name"], calorie=data["food_calorie"])
