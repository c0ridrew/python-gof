from injector import Injector

from clean_architecture.i_presenter import ICreateMenuPresenter
from clean_architecture.i_repository import IRepository
from clean_architecture.i_use_case import ICreateMenuUseCase
from clean_architecture.interactor import CreateMenuInteractor
from clean_architecture.presenter import CreateMenuPresenter
from clean_architecture.repository import Repository


class Dependency:
    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder):
        binder.bind(ICreateMenuPresenter, CreateMenuPresenter)
        binder.bind(IRepository, Repository)

    def resolve(self, cls):
        return self.injector.get(cls)