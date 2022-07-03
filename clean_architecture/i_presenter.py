from abc import ABC, abstractmethod

from clean_architecture.output_data import CreateMenuOutputData


class ICreateMenuPresenter(ABC):
    @abstractmethod
    def complete(self, output_data: CreateMenuOutputData):
        pass
