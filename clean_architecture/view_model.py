from dataclasses import dataclass


@dataclass()
class CreateMenuViewModel:
    result_menu_name: str = ""
    result_calorie: int = 0
