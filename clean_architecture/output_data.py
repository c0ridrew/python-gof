from dataclasses import dataclass


@dataclass()
class CreateMenuOutputData:
    menu_name: str
    calorie: int
