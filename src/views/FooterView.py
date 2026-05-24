import curses

class FooterView:
    def __init__(self, win):
        self.win = win
        self.__render()
     
    def __render(self):
        self.win.bkgd(' ', curses.color_pair(3))
        self.win.addstr(0, 0, "Footer", curses.color_pair(2))
        self.win.refresh()   
    