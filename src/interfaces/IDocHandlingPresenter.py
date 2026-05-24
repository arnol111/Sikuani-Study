from abc import ABC, abstractmethod


class IDocHandlingPresenter(ABC):

    @abstractmethod
    def start(self) -> None:
        pass
