import curses
import logging
from src.models import KeyMapper
from src.models.KeyMapper import KeyEvent
from src.interfaces.IContentView import IContentView


class ContentView(IContentView):
    def __init__(self, win):
        self.__win = win

    def get_input(self) -> KeyEvent:
        k = self.__win.getch()
        if k == curses.KEY_UP:
            return KeyEvent(KeyMapper.MOVE_UP)
        if k == curses.KEY_DOWN:
            return KeyEvent(KeyMapper.MOVE_DOWN)
        if k == curses.KEY_LEFT:
            return KeyEvent(KeyMapper.MOVE_LEFT)
        if k == curses.KEY_RIGHT:
            return KeyEvent(KeyMapper.MOVE_RIGHT)
        if k in (curses.KEY_BACKSPACE, 127):
            return KeyEvent(KeyMapper.BACKSPACE)
        if k in (10, ord("\n")):
            return KeyEvent(KeyMapper.ENTER)
        if 32 <= k <= 126:
            return KeyEvent(KeyMapper.PRINTABLE, char=chr(k))
        return KeyEvent(KeyMapper.UNKNOWN)

    def render_ch(self, pos_y: int, pos_x: int, pressedKey: str) -> None:
        row = self.__win.instr(pos_y, 0).decode("utf-8").rstrip()
        self.__win.refresh()
        row = row[:pos_x] + pressedKey + row[pos_x:]
        self.__win.addstr(pos_y, pos_x, pressedKey, curses.color_pair(2))
        self.__win.move(pos_y, pos_x + 1)
        self.__win.refresh()

    def render_new_line(self, pos_y: int, pos_x: int) -> None:
        row = self.__win.instr(pos_y, 0).decode("utf-8").rstrip()
        before = row[:pos_x]
        after = row[pos_y:]
        if len(before.strip()) > 0:
            self.__win.addstr(pos_y, pos_x, before, curses.color_pair(2))
        self.__win.move(pos_y, pos_x)
        self.__win.refresh()

    def render_remove_ch(self, pos_y: int, pos_x: int) -> None:
        logging.debug(f"pos x = {pos_x}")
        if pos_x > 0:
            self.__win.delch(pos_y, pos_x-1)
            pos_x -= 1
            self.__win.move(pos_y, pos_x)

        if pos_x == 0 and pos_y > 0:
            self.__win.deleteln()
            self.__win.refresh()
            self.__win.move(pos_y, pos_x)
