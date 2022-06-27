class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class FactoryConfig(metaclass=SingletonMeta):
    def __init__(self, log_level="INFO"):
        self.log_level = log_level


class Factory_A:
    def __init__(self, config):
        self.config = config

    def show_config(self):
        return self.config


class Factory_B:
    def __init__(self, config):
        self.config = config

    def show_config(self):
        return self.config


def main():
    config = FactoryConfig(log_level="DEBUG")
    factory_a = Factory_A(config)
    print(vars(factory_a.show_config()))

    bad_config = FactoryConfig(log_level="WARNING")
    factory_b = Factory_B(bad_config)
    print(vars(factory_b.show_config()))


if __name__ == "__main__":
    main()
