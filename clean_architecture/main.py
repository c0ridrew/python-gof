import argparse

from clean_architecture.controller import CreateMenuController
from clean_architecture.dependency import Dependency
from clean_architecture.view import CreateMenuView

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--menu", choices=["curry", "nikujyaga"])
    args = parser.parse_args()

    dependency = Dependency()
    controller = dependency.resolve(CreateMenuController)
    controller.create_menu(args.menu)
    CreateMenuView().show_result()
