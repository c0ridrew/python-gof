from abc import ABC, abstractmethod

from clean_architecture.entity import Ingredient, Seasoning


class IRepository(ABC):
    @abstractmethod
    def get_onion() -> Ingredient:
        pass

    @abstractmethod
    def get_potato() -> Ingredient:
        pass

    @abstractmethod
    def get_carrot() -> Ingredient:
        pass

    @abstractmethod
    def get_curry_powder() -> Seasoning:
        pass

    @abstractmethod
    def get_soy_sauce() -> Seasoning:
        pass

    @abstractmethod
    def get_sake() -> Seasoning:
        pass
