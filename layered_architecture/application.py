import argparse

from layered_architecture.model import Chef, MenuOption


def main(menu_option: str):
    chef = Chef()
    menu_option = MenuOption(menu_option)
    menu = chef.cook_menu(menu_option)
    return menu


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--menu", choices=["curry", "nikujyaga"])
    args = parser.parse_args()
    main(args.menu)
