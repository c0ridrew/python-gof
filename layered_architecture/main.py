import argparse

from layered_architecture.presentation import CreateMenuPresentation

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--menu", choices=["curry", "nikujyaga"])
    args = parser.parse_args()
    CreateMenuPresentation().show_result(args.menu)
