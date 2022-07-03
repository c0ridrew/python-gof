from clean_architecture.i_presenter import ICreateMenuPresenter
from clean_architecture.output_data import CreateMenuOutputData
from clean_architecture.view_model import CreateMenuViewModel


class CreateMenuPresenter(ICreateMenuPresenter):
    @staticmethod
    def complete(output_data: CreateMenuOutputData):
        menu_name = output_data.menu_name
        calorie = output_data.calorie
        view_model = CreateMenuViewModel(menu_name=menu_name, calorie=calorie)
        print(f"{view_model.menu_name} is cooked, calorie: {view_model.calorie}")