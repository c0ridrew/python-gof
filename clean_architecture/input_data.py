import enum


class InputMenuOption(enum.Enum):
    curry = "curry"
    nikujyaga = "nikujyaga"


class CreateMenuInputData:
    def __init__(self, input_menu: str) -> None:
        if input_menu == InputMenuOption.curry.value:
            self.menu = InputMenuOption.curry
        elif input_menu == InputMenuOption.nikujyaga.value:
            self.menu = InputMenuOption.nikujyaga
        else:
            raise ValueError(f"invalid input_menu: {input_menu}")
