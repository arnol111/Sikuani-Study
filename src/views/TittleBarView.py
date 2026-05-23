import curses


class TitleBarView:
    def __init__(self, window):
        self.window = window
        self.__render()
        
    def __render(self):
        self.window.bkgd(' ', curses.color_pair(3))
        self.window.addstr(0, 0, "Title Bar", curses.color_pair(3))
        self.window.refresh()
