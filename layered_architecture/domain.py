import enum
from dataclasses import dataclass, field
from typing import Callable, List, Tuple

from layered_architecture.infrastructure import FoodData, FoodType, Infrastructure


class MenuOption(enum.Enum):
    curry = "curry"
    nikujyaga = "nikujyaga"


# 食材データクラス
@dataclass()
class Ingredient:
    name: str
    calorie: int
    is_cut: bool = False
    is_cooked: bool = False


# 調味料データクラス
@dataclass()
class Seasoning:
    name: str
    calorie: int
    is_added: bool = False


# カレーデータクラス
@dataclass()
class Curry:
    name = "curry"
    calorie: int
    ingredints: List[Ingredient]
    seasonings: List[Seasoning]


# 肉じゃがデータクラス
@dataclass()
class Nikujyaga:
    name = "nikujyaga"
    calorie: int
    ingredints: List[Ingredient]
    seasonings: List[Seasoning]


# データ取得クラス
@dataclass()
class DataFetcher:
    infrastructure: Infrastructure = Infrastructure()
    ingredients: List[Ingredient] = field(default_factory=list)
    seasonings: List[Seasoning] = field(default_factory=list)

    # 呼び出し関数
    def fetch(self, menu: MenuOption) -> Tuple[List[Ingredient], List[Seasoning]]:
        if menu == MenuOption.curry:
            self._fetch_curry_ingredient()
        elif menu == MenuOption.nikujyaga:
            self._fetch_nikujyaga_ingredient()
        else:
            raise ValueError(f"Unsupported Menu {menu}")
        return self.ingredients, self.seasonings

    # カレーデータ取得
    def _fetch_curry_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(self.infrastructure.get_curry_powder)

    # 肉じゃがデータ取得
    def _fetch_nikujyaga_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(self.infrastructure.get_sake)
        self._fetch_data(self.infrastructure.get_soy_sauce)

    # 共通データ取得
    def _fetch_common_ingredient(self):
        self._fetch_data(self.infrastructure.get_carrot)
        self._fetch_data(self.infrastructure.get_potato)
        self._fetch_data(self.infrastructure.get_onion)
        self._fetch_data(self.infrastructure.get_chicken)

    # データ取得共通処理
    def _fetch_data(self, get_func: Callable[[], FoodData]):
        data = get_func()
        if data.type == FoodType.ingredient:
            self.ingredients.append(Ingredient(name=data.name, calorie=data.calorie))
        elif data.type == FoodType.seasoning:
            self.seasonings.append(Seasoning(name=data.name, calorie=data.calorie))
        else:
            raise ValueError(f"Invalid food_type of {data.type}")


@dataclass()
class Chef:
    is_water_boiled: bool = False

    # 料理をする
    def cook_menu(
        self,
        ingredients: List[Ingredient],
        seasonings: List[Seasoning],
        menu: MenuOption,
    ):
        self._cut_ingredient(ingredients)
        self._cook_ingredient(ingredients)
        self._boil_water()
        self._add_seasoning(seasonings)
        total_calorie = self._calc_total_calorie(ingredients, seasonings)

        if menu == MenuOption.curry:
            return Curry(
                calorie=total_calorie, ingredints=ingredients, seasonings=seasonings
            )
        elif menu == MenuOption.nikujyaga:
            return Nikujyaga(
                calorie=total_calorie, ingredints=ingredients, seasonings=seasonings
            )
        else:
            raise ValueError(f"Unsupported Menu: {menu}")

    # 食材を切る
    @staticmethod
    def _cut_ingredient(ingredients: List[Ingredient]):
        for ingredient in ingredients:
            ingredient.is_cut = True

    # 食材を炒める
    @staticmethod
    def _cook_ingredient(ingredients: List[Ingredient]):
        for ingredient in ingredients:
            ingredient.is_cooked = True

    # 調味料を加える
    @staticmethod
    def _add_seasoning(seasonings: List[Seasoning]):
        for seasoning in seasonings:
            seasoning.is_added = True

    # カロリーを計算する
    @staticmethod
    def _calc_total_calorie(ingredients, seasonings):
        return sum([i.calorie for i in ingredients + seasonings])

    # 水を加える
    def _boil_water(self):
        self.is_water_boiled = True
