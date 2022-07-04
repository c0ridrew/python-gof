from dataclasses import dataclass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass()
class CreateMenuViewModel(metaclass=Singleton):
    result_menu_name: str = ""
    result_calorie: int = 0
