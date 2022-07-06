from dataclasses import dataclass

from layered_architecture.domain import Chef, DataFetcher, MenuOption


@dataclass()
class CreateMenuApplication:
    def handle(self, menu_input: str):
        if menu_input == MenuOption.curry.value:
            menu = MenuOption.curry
        elif menu_input == MenuOption.nikujyaga.value:
            menu = MenuOption.nikujyaga
        else:
            raise ValueError(f"invalid menu: {menu_input}")

        ingredients, seasonings = DataFetcher().fetch(menu)
        return Chef().cook_menu(
            ingredients=ingredients, seasonings=seasonings, menu=menu
        )
