from abc import ABC, abstractmethod
from dataclasses import dataclass


def main():
    car = CarFactory()
    car.check_product(wheels_num=4)

    bike = BikeFactory()
    bike.check_product(wheels_num=2)


class Product(ABC):
    @abstractmethod
    def count_wheels() -> int:
        pass


@dataclass()
class Car(Product):
    wheels_num = 4

    def count_wheels(self) -> int:
        return self.wheels_num


@dataclass()
class Bike(Product):
    wheels_num = 2

    def count_wheels(self) -> int:
        return self.wheels_num


class Factory(ABC):
    def __init__(self) -> None:
        self.product = self.factory_method()

    def build(self) -> Product:
        if self.product is None:
            raise RuntimeError("product is None")
        return self.product

    def check_product(self, wheels_num: int):
        if self.product is None:
            raise RuntimeError("product is None")
        if self.product.count_wheels() != wheels_num:
            raise ValueError(f"this {self.product} does not have {wheels_num} wheels!")

    @abstractmethod
    def factory_method():
        pass


class CarFactory(Factory):
    def factory_method(self) -> Car:
        return Car()


class BikeFactory(Factory):
    def factory_method(self) -> Bike:
        return Bike()


if __name__ == "__main__":
    main()
