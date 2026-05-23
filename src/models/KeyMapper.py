from dataclasses import dataclass
from enum import Enum, auto

class KeyMapper(Enum):
    MOVE_UP        = auto()
    MOVE_DOWN      = auto()
    MOVE_LEFT      = auto()
    MOVE_RIGHT     = auto()
    BACKSPACE      = auto()
    ENTER          = auto()
    PRINTABLE      = auto()   # caracteres 32–126
    UNKNOWN        = auto()
    
@dataclass(frozen=True)
class KeyEvent:
    key: EditorKey
    char: str = ""   # solo se llena cuando key == PRINTABLE
    
    