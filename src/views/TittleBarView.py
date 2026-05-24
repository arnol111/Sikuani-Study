import curses


class TittleBarView:
    def __init__(self, win):
        self.win = win
        self.__render()

    def __render(self) -> None:
        self.win.bkgd(" ", curses.color_pair(3))
        self.win.addstr(0, 0, "Title Bar", curses.color_pair(3))
        self.win.refresh()
