import curses


class FooterView:
    def __init__(self, window):
        self.window = window
        self.__render()
        
    def __render(self):
        self.window.bkgd(' ', curses.color_pair(3))
        self.window.addstr(0, 0, "Footer", curses.color_pair(2))
        self.window.refresh()