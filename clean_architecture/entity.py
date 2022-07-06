import enum
from dataclasses import dataclass
from typing import List

from clean_architecture.input_data import CreateMenuInputData


@dataclass()
class Ingredient:
    name: str
    calorie: int
    is_cut: bool = False
    is_cooked: bool = False


@dataclass()
class Seasoning:
    name: str
    calorie: int
    is_added: bool = False


@dataclass()
class Curry:
    name = "curry"
    calorie: int
    ingredints: List[Ingredient]
    seasonings: List[Seasoning]


@dataclass()
class Nikujyaga:
    name = "nikujyaga"
    calorie: int
    ingredints: List[Ingredient]
    seasonings: List[Seasoning]


class MenuOption(enum.Enum):
    curry = "curry"
    nikujyaga = "nikujyaga"


@dataclass()
class Chef:
    is_water_boiled: bool = False

    # 料理をする
    def cook_menu(
        self,
        ingredients: List[Ingredient],
        seasonings: List[Seasoning],
        input_data: CreateMenuInputData,
    ):
        self._cut_ingredient(ingredients)
        self._cook_ingredient(ingredients)
        self._boil_water()
        self._add_seasoning(seasonings)
        total_calorie = self._calc_total_calorie(ingredients, seasonings)

        if input_data.menu == MenuOption.curry:
            return Curry(
                calorie=total_calorie, ingredints=ingredients, seasonings=seasonings
            )
        elif input_data.menu == MenuOption.nikujyaga:
            return Nikujyaga(
                calorie=total_calorie, ingredints=ingredients, seasonings=seasonings
            )
        else:
            raise ValueError(f"Unsupported Menu: {input_data.menu}")

    @staticmethod
    def _cut_ingredient(ingredients: List[Ingredient]):
        for ingredient in ingredients:
            ingredient.is_cut = True

    @staticmethod
    def _cook_ingredient(ingredients: List[Ingredient]):
        for ingredient in ingredients:
            ingredient.is_cooked = True

    @staticmethod
    def _add_seasoning(seasonings: List[Seasoning]):
        for seasoning in seasonings:
            seasoning.is_added = True

    @staticmethod
    def _calc_total_calorie(ingredients, seasonings):
        return sum([i.calorie for i in ingredients + seasonings])

    def _boil_water(self):
        self.is_water_boiled = True
