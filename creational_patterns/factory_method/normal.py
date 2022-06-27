from dataclasses import dataclass


def main():
    car = CarFactory().build()
    CarFactory.check_product(car)

    bike = BikeFactory().build()
    BikeFactory.check_product(bike)


@dataclass()
class Car:
    wheels_num = 4

    def count_wheels(self):
        return self.wheels_num


@dataclass()
class Bike:
    wheels_num = 2

    def count_wheels(self):
        return self.wheels_num


@dataclass()
class CarFactory:
    @staticmethod
    def build():
        return Car()

    @staticmethod
    def check_product(car: Car):
        if car.wheels_num != 4:
            raise ValueError("this car does not have 4 wheels!")


class BikeFactory:
    @staticmethod
    def build():
        return Bike()

    @staticmethod
    def check_product(bike: Bike):
        if bike.wheels_num != 2:
            raise ValueError("this bike does not have 2 wheels!")


if __name__ == "__main__":
    main()
