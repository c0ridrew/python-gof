from dataclasses import dataclass


@dataclass()
class CreateMenuViewModel:
    menu_name: str
    calorie: int
