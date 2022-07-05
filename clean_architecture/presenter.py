from clean_architecture.i_presenter import ICreateMenuPresenter
from clean_architecture.output_data import CreateMenuOutputData
from clean_architecture.view_model import CreateMenuViewModel


class CreateMenuPresenter(ICreateMenuPresenter):
    @staticmethod
    def complete(output_data: CreateMenuOutputData):
        menu_name = output_data.menu_name
        calorie = output_data.calorie
        CreateMenuViewModel(result_menu_name=menu_name, result_calorie=calorie)


class DevCreateMenuPresenter(ICreateMenuPresenter):
    @staticmethod
    def complete(output_data: CreateMenuOutputData):
        menu_name = output_data.menu_name
        calorie = output_data.calorie * 1000
        CreateMenuViewModel(result_menu_name=menu_name, result_calorie=calorie)
