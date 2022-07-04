from dataclasses import dataclass, field
from typing import Callable, List

from clean_architecture.entity import Curry, Ingredient, Nikujyaga, Seasoning
from clean_architecture.i_presenter import ICreateMenuPresenter
from clean_architecture.i_repository import IRepository
from clean_architecture.i_use_case import ICreateMenuUseCase
from clean_architecture.input_data import CreateMenuInputData, InputMenuOption
from clean_architecture.output_data import CreateMenuOutputData


@dataclass()
class DataFetcher:
    repository: IRepository
    ingredients: List[Ingredient] = field(default_factory=list)
    seasonings: List[Seasoning] = field(default_factory=list)

    def fetch(self, input_data: CreateMenuInputData):
        menu = input_data.menu
        if menu == InputMenuOption.curry:
            self._fetch_curry_ingredient()
        elif menu == InputMenuOption.nikujyaga:
            self._fetch_nikujyaga_ingredient()
        else:
            raise ValueError(f"Unsupported Menu {menu}")

    def _fetch_curry_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(self.repository.get_curry_powder)
        print("fetch curry ingeredients")

    def _fetch_nikujyaga_ingredient(self):
        self._fetch_common_ingredient()
        self._fetch_data(self.repository.get_sake)
        self._fetch_data(self.repository.get_soy_sauce)
        print("fetch nikujyaga ingeredients")

    def _fetch_common_ingredient(self):
        self._fetch_data(self.repository.get_carrot)
        self._fetch_data(self.repository.get_potato)
        self._fetch_data(self.repository.get_onion)

    def _fetch_data(self, get_func: Callable[[], Ingredient | Seasoning]):
        data = get_func()
        if isinstance(data, Ingredient):
            self.ingredients.append(Ingredient(name=data.name, calorie=data.calorie))
        elif isinstance(data, Seasoning):
            self.seasonings.append(Seasoning(name=data.name, calorie=data.calorie))
        else:
            raise ValueError(f"Invalid food_type of {data.food_type}")


@dataclass()
class Chef:
    is_water_boiled: bool = False

    def cook_menu(self, input_data: CreateMenuInputData, data_fetcher: DataFetcher):
        menu = input_data.menu
        data_fetcher.fetch(input_data)
        ingredients = data_fetcher.ingredients
        seasonings = data_fetcher.seasonings
        self._cut_ingredient(ingredients)
        self._cook_ingredient(ingredients)
        self._boil_water()
        self._add_seasoning(seasonings)
        total_calorie = self._calc_total_calorie(ingredients, seasonings)

        if menu == InputMenuOption.curry:
            return Curry(
                calorie=total_calorie, ingredints=ingredients, seasonings=seasonings
            )
        elif menu == InputMenuOption.nikujyaga:
            return Nikujyaga(
                calorie=total_calorie, ingredints=ingredients, seasonings=seasonings
            )
        else:
            raise ValueError(f"Unsupported Menu: {menu}")

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


@dataclass()
class CreateMenuInteractor(ICreateMenuUseCase):
    repository: IRepository
    presenter: ICreateMenuPresenter

    def handle(self, input_data: CreateMenuInputData):
        data_fetcher = DataFetcher(self.repository)
        menu = Chef().cook_menu(input_data=input_data, data_fetcher=data_fetcher)

        output_data = CreateMenuOutputData(menu_name=menu.name, calorie=menu.calorie)
        self.presenter.complete(output_data)
