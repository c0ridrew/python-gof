import argparse

from clean_architecture.controller import CreateMenuController
from clean_architecture.dependency import DevDependency
from clean_architecture.view import CreateMenuView


def run(dependency):
    controller = dependency.resolve(CreateMenuController)
    controller.create_menu(args.menu)
    CreateMenuView().show_result()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--menu", choices=["curry", "nikujyaga"])
    args = parser.parse_args()

    # dependency = Dependency()
    # run(dependency)
    dev_dependency = DevDependency()
    run(dev_dependency)
