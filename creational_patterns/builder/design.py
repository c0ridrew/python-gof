from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass()
class Engine:
    type: str


@dataclass()
class Transmission:
    type: str


@dataclass()
class Wheel:
    type: str


@dataclass()
class Car:
    engine: Optional[Engine] = None
    transmission: Optional[Transmission] = None
    wheel: Optional[Wheel] = None


@dataclass()
class Bike:
    engine: Optional[Engine] = None
    transmission: Optional[Transmission] = None
    wheel: Optional[Wheel] = None


class AbstractBuidler(ABC):
    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_transmission(self):
        pass

    @abstractmethod
    def build_wheel(self):
        pass


@dataclass()
class CarBuilder(AbstractBuidler):
    car: Car = Car()

    @classmethod
    def build(cls) -> Car:
        if (
            cls.car.engine is None
            or cls.car.transmission is None
            or cls.car.wheel is None
        ):
            raise ValueError("some parts are missing")
        return cls.car

    @classmethod
    def build_engine(cls):
        cls.car.engine = Engine("auto")

    @classmethod
    def build_transmission(cls):
        cls.car.transmission = Transmission("auto")

    @classmethod
    def build_wheel(cls, wheel: Wheel):
        cls.car.wheel = Wheel("four")


@dataclass()
class BikeBuilder(AbstractBuidler):
    bike: Bike = Bike()

    @classmethod
    def build(cls) -> Bike:
        if (
            cls.bike.engine is None
            or cls.bike.transmission is None
            or cls.bike.wheel is None
        ):
            raise ValueError("some parts are missing")
        return cls.bike

    @classmethod
    def build_engine(cls):
        cls.bike.engine = Engine("auto")

    @classmethod
    def build_transmission(cls):
        cls.bike.transmission = Transmission("auto")

    @classmethod
    def build_wheel(cls, wheel: Wheel):
        cls.bike.wheel = Wheel("four")


class Director:
    @staticmethod
    def construct(builder: AbstractBuidler):
        builder.build_engine()
        builder.build_transmission()
        builder.build_wheel()

        return builder.build()


def main(target_product: str):
    if target_product == "Car":
        return Director.construct(CarBuilder())
    elif target_product == "Bike":
        return Director.construct(BikeBuilder())


if __name__ == "__main__":
    # 車を作る場合
    main("Car")
    # バイクを作る場合
    main("Bike")
