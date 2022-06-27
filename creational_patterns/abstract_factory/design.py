from abc import ABC, abstractmethod
from typing import Tuple


class AbstractCar(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class CarA(AbstractCar):
    def start(self):
        # some process
        pass

    def stop(self):
        # some process
        pass


class CarB(AbstractCar):
    def start(self):
        # some process
        pass

    def stop(self):
        # some process
        pass


class AbstractBike(ABC):
    @abstractmethod
    def proceed(self):
        pass

    @abstractmethod
    def complete(self):
        pass


class BikeA(AbstractBike):
    def proceed(self):
        # some process
        pass

    def complete(self):
        # some process
        pass


class BikeB(AbstractBike):
    def proceed(self):
        # some process
        pass

    def complete(self):
        # some process
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def build_car(self) -> AbstractCar:
        pass

    @abstractmethod
    def build_bike(self) -> AbstractBike:
        pass


class FactoryA(AbstractFactory):
    def build_car(self) -> CarA:
        return CarA()

    def build_bike(self) -> BikeA:
        return BikeA()


class FactoryB(AbstractFactory):
    def build_car(self) -> CarB:
        return CarB()

    def build_bike(self) -> BikeB:
        return BikeB()


def main(
    factory: AbstractFactory,
) -> Tuple[AbstractCar, AbstractBike]:
    car = factory.build_car()
    bike = factory.build_bike()
    return car, bike


if __name__ == "__main__":
    # 工場Aで作成する場合
    main(FactoryA())
    # 工場Bで作成する場合
    main(FactoryB())
