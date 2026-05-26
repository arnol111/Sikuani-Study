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
        
        if k == 19:
            return KeyEvent(KeyMapper.SAVE_DOCUMENT)
        if k == 15:  # Ctrl+O
            return KeyEvent(KeyMapper.LOAD_DOCUMENT)
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

    def render_remove_ch(self, pos_y: int, pos_x: int, last_location : int = 0) -> None:
        if pos_x > 0:
            self.__win.delch(pos_y, pos_x-1)
            pos_x -= 1
            self.__win.move(pos_y, pos_x)

        elif pos_x == 0 and pos_y > 0:
            self.__win.deleteln()
            self.__win.refresh()
            pos_y -= 1
            pos_x = last_location
            self.__win.move(pos_y, pos_x)

    def prompt_file_path(self, message: str) -> str:
        high, width = self.__win.getmaxyx()
        prompt_y = high - 1
        self.__win.move(prompt_y, 0)
        self.__win.clrtoeol()
        self.__win.addstr(prompt_y, 0, message)
        self.__win.refresh()
        curses.echo()
        curses.curs_set(1)
        file_path = self.__win.getstr(prompt_y, len(message), width - len(message) - 1)
        curses.noecho()
        curses.curs_set(0)
        self.__win.move(prompt_y, 0)
        self.__win.clrtoeol()
        self.__win.refresh()
        return file_path.decode("utf-8").strip()

    def render_status(self, message: str) -> None:
        high, width = self.__win.getmaxyx()
        status_y = high - 1
        self.__win.move(status_y, 0)
        self.__win.clrtoeol()
        self.__win.addstr(status_y, 0, message, curses.color_pair(2))
        self.__win.refresh()
            
            
