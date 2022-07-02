import argparse

from layered_architecture.model import Chef


def main(menu_option: str):
    chef = Chef()
    menu = chef.cook_menu(menu_option)
    print(f"{menu_option} is cooked, calorie: {menu.calorie}")
    return menu


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--menu", choices=["curry", "nikujyaga"])
    args = parser.parse_args()
    main(args.menu)
