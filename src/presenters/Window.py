import curses
from src.interfaces import IDocumentHandling
from src.interfaces import IWindow

##interfaces.IDocumentHandling import IDocumentHandling  # ✅


class Window(IWindow):

    def __init__(self, stdscr, doc_handler: IDocumentHandling):
        self.stdscr = stdscr
        self.doc_handler = doc_handler
        self.footer = None
        self.title_bar = None

    def start(self):
        self.styles()
        win = self.stdscr
        win.bkgd(' ', curses.color_pair(1))
        high, width = win.getmaxyx()

        # Layout Windows
        self.title_bar = curses.newwin(1, width,0,0)
        self.content = curses.newwin(high-2, width,1,0)
        self.footer = curses.newwin(1,width,high-1,0)

        self._draw_title_bar()
        self._draw_footer()
        self.content.refresh()

        self.doc_handler.win = self.content

        #win.move(1,0)
        self.doc_handler.write_character()

    def _draw_title_bar(self):
        self.title_bar.bkgd(' ', curses.color_pair(3))
        self.title_bar.addstr(0, 0, "Title Bar", curses.color_pair(3))
        self.title_bar.refresh()

    def _draw_footer(self):
        self.footer.bkgd(' ', curses.color_pair(3))
        self.footer.addstr(0, 0, "Footer", curses.color_pair(2))
        self.footer.refresh()

    def refresh_footer(self):
        self._draw_footer()

    def styles(self):
        curses.start_color()
        curses.use_default_colors()  # ← esto es clave en muchas terminales

        if not curses.has_colors():
            raise RuntimeError("Tu terminal no soporta colores")

        curses.init_pair(1, -1, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_CYAN)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLUE)