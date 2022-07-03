from dataclasses import dataclass

from clean_architecture.i_use_case import ICreateMenuUseCase
from clean_architecture.input_data import CreateMenuInputData


@dataclass()
class CreateMenuController:
    create_menu_usecase: ICreateMenuUseCase

    def create_menu(self, input_menu: str):
        input_data = CreateMenuInputData(input_menu=input_menu)
        self.create_menu_usecase.handle(input_data)
