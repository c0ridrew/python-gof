class CarA:
    def start(self):
        # some process
        pass

    def stop(self):
        # some process
        pass


class CarB:
    def start(self):
        # some process
        pass

    def stop(self):
        # some process
        pass


class BikeA:
    def proceed(self):
        # some process
        pass

    def complete(self):
        # some process
        pass


class BikeB:
    def proceed(self):
        # some process
        pass

    def complete(self):
        # some process
        pass


def main(
    factory_type: str,
):
    if factory_type == "A":
        return CarA, BikeA
    elif factory_type == "B":
        return CarB, BikeB


if __name__ == "__main__":
    # 工場Aで作成する場合
    main("A")
    # 工場Bで作成する場合
    main("B")
