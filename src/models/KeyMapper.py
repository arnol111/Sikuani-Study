from enum import Enum, auto
from dataclasses import dataclass

class KeyMapper(Enum):
    MOVE_UP       = auto()
    MOVE_DOWN     = auto()
    MOVE_LEFT     = auto()
    MOVE_RIGHT    = auto()
    BACKSPACE     = auto()
    ENTER         = auto()
    PRINTABLE     = auto()
    UNKNOWN       = auto()
    SAVE_DOCUMENT = auto()
    LOAD_DOCUMENT = auto()

@dataclass(frozen=True)
class KeyEvent:
    key: KeyMapper
    char: str = ""   # solo se llena cuando key == PRINTABLE