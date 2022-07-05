from injector import Injector, Module

from clean_architecture.i_presenter import ICreateMenuPresenter
from clean_architecture.i_repository import IRepository
from clean_architecture.i_use_case import ICreateMenuUseCase
from clean_architecture.interactor import CreateMenuInteractor, DevCreateMenuInteractor
from clean_architecture.presenter import CreateMenuPresenter, DevCreateMenuPresenter
from clean_architecture.repository import DevRepository, Repository


class Dependency(Module):
    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder):
        binder.bind(ICreateMenuPresenter, to=CreateMenuPresenter)
        binder.bind(IRepository, to=Repository)
        binder.bind(ICreateMenuUseCase, to=CreateMenuInteractor)

    def resolve(self, cls):
        return self.injector.get(cls)


class DevDependency(Module):
    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder):
        binder.bind(ICreateMenuPresenter, to=DevCreateMenuPresenter)
        binder.bind(IRepository, to=DevRepository)
        binder.bind(ICreateMenuUseCase, to=DevCreateMenuInteractor)

    def resolve(self, cls):
        return self.injector.get(cls)
