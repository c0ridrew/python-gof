from dataclasses import dataclass


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
    engine: Engine
    transmission: Transmission
    wheel: Wheel


@dataclass()
class Bike:
    engine: Engine
    transmission: Transmission
    wheel: Wheel


def main(target_product: str):
    if target_product == "Car":
        gasoline = Engine("gasoline")
        auto = Transmission("auto")
        four_wheels = Wheel("four")
        return Car(gasoline, auto, four_wheels)

    elif target_product == "Bike":
        diesel = Engine("diesel")
        manual = Transmission("manual")
        two_wheels = Wheel("two")
        return Car(diesel, manual, two_wheels)


if __name__ == "__main__":
    # 車を作る場合
    main("Car")
    # バイクを作る場合
    main("Bike")
