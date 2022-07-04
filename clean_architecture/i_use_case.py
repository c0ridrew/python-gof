from abc import ABC, abstractmethod

from clean_architecture.input_data import CreateMenuInputData


class ICreateMenuUseCase(ABC):
    @abstractmethod
    def handle(self, input_data: CreateMenuInputData):
        pass
