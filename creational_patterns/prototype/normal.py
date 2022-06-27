def main():
    lexus_1 = Car("Lexus")
    lexus_2 = Car("Lexus")


class Car:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    main()
