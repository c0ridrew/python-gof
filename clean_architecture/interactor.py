from dataclasses import dataclass, field
from typing import Callable, List, Tuple

from injector import inject

from clean_architecture.entity import Chef, Ingredient, MenuOption, Seasoning
from clean_architecture.i_presenter import ICreateMenuPresenter
from clean_architecture.i_repository import IRepository
from clean_architecture.i_use_case import ICreateMenuUseCase
from clean_architecture.input_data import CreateMenuInputData
from clean_architecture.output_data import CreateMenuOutputData


@dataclass()
class DataFetcher:
    repository: IRepository
    ingredients: List[Ingredient] = field(default_factory=list)
    seasonings: List[Seasoning] = field(default_factory=list)

    def fetch(
        self, input_data: CreateMenuInputData
    ) -> Tuple[List[Ingredient], List[Seasoning]]:
        if input_data.menu == MenuOption.curry.value:
            self._fetch_curry_ingredient()
        elif input_data.menu == MenuOption.nikujyaga.value:
            self._fetch_nikujyaga_ingredient()
        else:
            raise ValueError(f"Unsupported Menu {input_data.menu}")
        return self.ingredients, self.seasonings

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


@inject
@dataclass()
class CreateMenuInteractor(ICreateMenuUseCase):
    repository: IRepository
    presenter: ICreateMenuPresenter

    def handle(self, input_data: CreateMenuInputData):
        ingredients, seasonings = DataFetcher(self.repository).fetch(input_data)
        menu = Chef().cook_menu(
            ingredients=ingredients, seasonings=seasonings, input_data=input_data
        )

        output_data = CreateMenuOutputData(menu_name=menu.name, calorie=menu.calorie)
        self.presenter.complete(output_data)


@inject
@dataclass()
class DevCreateMenuInteractor(ICreateMenuUseCase):
    repository: IRepository
    presenter: ICreateMenuPresenter

    def handle(self, input_data: CreateMenuInputData):
        ingredients, seasonings = DataFetcher(self.repository).fetch(input_data)
        menu = Chef().cook_menu(
            ingredients=ingredients, seasonings=seasonings, input_data=input_data
        )

        output_data = CreateMenuOutputData(menu_name=menu.name, calorie=menu.calorie)
        self.presenter.complete(output_data)
