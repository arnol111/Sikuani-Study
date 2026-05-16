import curses
from src.interfaces import IDocumentHandling
from src.interfaces import IWindow

##interfaces.IDocumentHandling import IDocumentHandling  # ✅


class Window(IWindow):

    def __init__(self, stdscr, doc_handler: IDocumentHandling):
        self.stdscr = stdscr
        self.doc_handler = doc_handler

    def start(self):

        win = self.stdscr
        win.bkgd(' ', curses.color_pair(1))

        high, width = win.getmaxyx()

        # derwin(nlines, ncols, begin_y, begin_x)
        task_bar = win.derwin(1, width,0, 0)
        task_bar.bkgd(' ', curses.color_pair(3))
        task_bar.addstr(0, 0, "BARRA DE TAREAS",curses.color_pair(3))
        task_bar.refresh()

        # derwin(nlines, ncols, begin_y, begin_x)
        foot_bar = win.derwin(1, width, high-1, 0)
        foot_bar.bkgd(' ', curses.color_pair(3))
        foot_bar.addstr(0, 0, "Footer",curses.color_pair(3))
        foot_bar.refresh()

        win.move(1,0)
        document = ""
        self.doc_handler.write_character()

