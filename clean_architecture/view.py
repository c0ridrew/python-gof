from clean_architecture.view_model import CreateMenuViewModel


class CreateMenuView:
    def show_result(self):
        view_model = CreateMenuViewModel()
        print(vars(view_model))
        print(f"menu: {view_model.result_menu_name} is cooked!")
        print(f"calorie: {view_model.result_calorie}")
