from dataclasses import dataclass

from layered_architecture.application import CreateMenuApplication


@dataclass()
class CreateMenuPresentation:
    application: CreateMenuApplication = CreateMenuApplication()

    def show_result(self, menu_input: str):
        print(f"start cooking {menu_input}")
        result = self.application.handle(menu_input)
        print(f"menu: {result.name} is cooked!")
        print(f"calorie: {result.calorie}")
