import enum
from dataclasses import dataclass, field
from typing import Callable, List

from layered_architecture.infrastructure import (
    FoodData,
    FoodType,
    get_carrot,
    get_curry_powder,
    get_onion,
    get_potato,
    get_sake,
    get_soy_sauce,
)


# 料理オプション
class MenuOption(enum.Enum):
    curry = "curry"
    nikujyaga = "nikujyaga"


# 食材クラス
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

    def from_data(self, data: FoodData):
        self.name = data.food_name
        self.calorie = data.food_calorie
        return self


@dataclass()
class Curry:
    name = "curry"
    calorie: int


@dataclass()
class Nikujyaga:
    name = "nikujyaga"
    calorie: int


@dataclass()
class DataFetcher:
    ingredients: List[Ingredient] = field(default_factory=list)
    seasonings: List[Seasoning] = field(default_factory=list)

    def fetch(self, menu: str):
        if menu == MenuOption.curry.value:
            self._fetch_curry_ingredient()
        elif menu == MenuOption.nikujyaga.value:
            self._fetch_nikujyaga_ingredient()
        else:
            raise ValueError(f"Unsupported Menu {menu}")

    def _fetch_curry_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(get_curry_powder)
        print("fetch curry ingeredients")

    def _fetch_nikujyaga_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(get_sake)
        self._fetch_data(get_soy_sauce)
        print("fetch nikujyaga ingeredients")

    def _fetch_common_ingredient(self):
        self._fetch_data(get_carrot)
        self._fetch_data(get_potato)
        self._fetch_data(get_onion)

    def _fetch_data(self, get_func: Callable):
        data = get_func()
        if data.food_type == FoodType.ingredient.value:
            self.ingredients.append(
                Ingredient(name=data.food_name, calorie=data.food_calorie)
            )
        elif data.food_type == FoodType.seasoning.value:
            self.seasonings.append(
                Seasoning(name=data.food_name, calorie=data.food_calorie)
            )
        else:
            raise ValueError(f"Invalid food_type of {data.food_type}")


@dataclass()
class Chef:
    data_fetcher = DataFetcher()
    is_water_boiled: bool = False

    def cook_menu(self, menu: str):
        self.data_fetcher.fetch(menu)
        ingredients = self.data_fetcher.ingredients
        seasonings = self.data_fetcher.seasonings
        self._cut_ingredient(ingredients)
        self._cook_ingredient(ingredients)
        self._boil_water()
        self._add_seasoning(seasonings)
        total_calorie = self._calc_total_calorie(ingredients, seasonings)

        if menu == MenuOption.curry.value:
            return Curry(calorie=total_calorie)
        elif menu == MenuOption.nikujyaga.value:
            return Nikujyaga(calorie=total_calorie)
        else:
            raise ValueError("Unsupported Menu")

    @staticmethod
    def _cut_ingredient(ingredients: List[Ingredient]):
        for ingredient in ingredients:
            ingredient.is_cut = True
            print(f"cut {ingredient.name}")

    @staticmethod
    def _cook_ingredient(ingredients: List[Ingredient]):
        for ingredient in ingredients:
            ingredient.is_cooked = True
            print(f"cook {ingredient.name}")

    @staticmethod
    def _add_seasoning(seasonings: List[Seasoning]):
        for seasoning in seasonings:
            seasoning.is_added = True
            print(f"add {seasoning.name}")

    @staticmethod
    def _calc_total_calorie(ingredients, seasonings):
        return sum([i.calorie for i in ingredients + seasonings])

    def _boil_water(self):
        self.is_water_boiled = True
        print("boil water")
