from dataclasses import dataclass

from injector import inject

from clean_architecture.i_use_case import ICreateMenuUseCase
from clean_architecture.input_data_series import CreateMenuInputDataSeries


@inject
@dataclass()
class CreateMenuController:
    create_menu_usecase: ICreateMenuUseCase

    def create_menu(self, input_menu: str):
        input_data = CreateMenuInputDataSeries(input_menu)
        self.create_menu_usecase.handle(input_data)
