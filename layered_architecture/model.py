import enum
from abc import ABC
from dataclasses import dataclass, field
from typing import Callable, List

from layered_architecture.infrastructure import (
    get_carrot,
    get_curry_powder,
    get_onion,
    get_potato,
    get_sake,
    get_soy_sauce,
)


class MenuOption(enum.Enum):
    curry = enum.auto()
    nikujyaga = enum.auto()


# 食材クラス
@dataclass()
class Ingredient:
    name: str = ""
    calorie: int = 0
    is_cut: bool = False
    is_cooked: bool = False


@dataclass()
class IngredientData:
    food_name: str
    food_calorie: int

    def to_model(self) -> Ingredient:
        return Ingredient(name=self.food_name, calorie=self.food_calorie)


@dataclass()
class AbstractMenu(ABC):
    ingredients: List[Ingredient]
    calorie: int


@dataclass()
class Curry(AbstractMenu):
    ingredients: List[Ingredient]
    calorie: int


@dataclass()
class Nikujyaga(AbstractMenu):
    ingredients: List[Ingredient]
    calorie: int


@dataclass()
class DataFetcher:
    ingredients: List[Ingredient] = field(default_factory=list)

    def fetch(self, menu: MenuOption) -> List[Ingredient]:
        if menu == MenuOption.curry:
            self._fetch_curry_ingredient()
        elif menu == MenuOption.nikujyaga:
            self._fetch_nikujyaga_ingredient()
        else:
            ValueError("Unsupported Menu")
        return self.ingredients

    def _fetch_curry_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(get_curry_powder)

    def _fetch_nikujyaga_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(get_sake)
        self._fetch_data(get_soy_sauce)

    def _fetch_common_ingredient(self):
        self._fetch_data(get_carrot)
        self._fetch_data(get_potato)
        self._fetch_data(get_onion)

    def _fetch_data(self, get_func: Callable):
        self.ingredients.append(IngredientData(**get_func()).to_model())


@dataclass()
class Chef:
    data_fetcher = DataFetcher()
    is_water_boiled: bool = False
    ingredients: List[Ingredient] = field(default_factory=list)

    def cook_menu(self, menu: MenuOption):
        self.ingredients = self.data_fetcher.fetch(menu)
        self._cut_ingredient()
        self._cook_ingredient()
        self._boil_water()
        total_calorie = self._calc_total_calorie()

        if menu == MenuOption.curry:
            return Curry(ingredients=self.ingredients, calorie=total_calorie)
        elif menu == MenuOption.nikujyaga:
            return Nikujyaga(ingredients=self.ingredients, calorie=total_calorie)
        else:
            ValueError("Unsupported Menu")

    def _cut_ingredient(self):
        for ingredient in self.ingredients:
            ingredient.is_cut = True
            print(f"cut {ingredient.name}")

    def _cook_ingredient(self):
        for ingredient in self.ingredients:
            ingredient.is_cooked = True
            print(f"cook {ingredient.name}")

    def _calc_total_calorie(self):
        return sum([i.calorie for i in self.ingredients])

    def _boil_water(self):
        self.is_water_boiled = True
        print("boil water")


def main():
    pass
