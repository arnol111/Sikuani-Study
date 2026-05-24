from abc import ABC, abstractmethod
from src.models.KeyMapper import KeyEvent


class IContentView(ABC):

    @abstractmethod
    def get_input(self) -> KeyEvent:
        pass

    @abstractmethod
    def render_ch(self, pos_y: int, pos_x: int, pressedKey: str) -> None:
        pass

    @abstractmethod
    def render_new_line(self, pos_y: int, pos_x: int) -> None:
        pass

    @abstractmethod
    def render_remove_ch(self, pos_y: int, pos_x: int) -> None:
        pass
