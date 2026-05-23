import curses
from models.services import DocumentServices
from models import DocumentText
from src.interfaces import IDocumentHandling
from src.interfaces import IWindow
from views import ContainerView, FooterView, TittleBarView

##interfaces.IDocumentHandling import IDocumentHandling  # ✅


class Window(IWindow):

    def __init__(self, stdscr, file_path: str = ""):
        self.stdscr = stdscr
        self.file_path = file_path

    def start(self):
        self.__styles()
        win = self.stdscr
        win.bkgd(" ", curses.color_pair(1))
        high, width = win.getmaxyx()

        # Layout Windows
        title_bar = curses.newwin(1, width, 0, 0)
        content = curses.newwin(high - 2, width, 1, 0)
        footer = curses.newwin(1, width, high - 1, 0)

        FooterView(footer)
        ContainerView(content)
        TittleBarView(title_bar)

        content.keypad(True)

        doc_service = DocumentServices()
        lines = doc_service.load(self.file_path) if self.file_path else [""]
        document = DocumentText(line = lines)
        
        # win.move(1,0)
        document_handling = DocumentHandling(document, content)
        document_handling.start()
        
    def refresh_footer(self):
        self._draw_footer()

    def __styles(self):
        curses.start_color()
        curses.use_default_colors()  # ← esto es clave en muchas terminales

        if not curses.has_colors():
            raise RuntimeError("Tu terminal no soporta colores")

        curses.init_pair(1, -1, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_CYAN)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLUE)
