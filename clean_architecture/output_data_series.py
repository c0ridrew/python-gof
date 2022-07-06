from dataclasses import dataclass


@dataclass()
class CreateMenuOutputDataSeries:
    menu_name: str
    calorie: int
