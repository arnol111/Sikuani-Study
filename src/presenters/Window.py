import curses
from src.presenters.Doc_HandlingPresenter import Doc_HandlingPresenter
from src.models.services import DocumentServices
from src.interfaces import IWindow
from src.views import FooterView, TittleBarView, ContentView

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

        # Validar depenencias de inyecciones
        FooterView(footer)
        TittleBarView(title_bar)

        # Modelo
        service = DocumentServices()
        document = service.load(self.file_path) 
        
        content.keypad(True)
        content.refresh()
        doc_handling_presenter =  Doc_HandlingPresenter(document, ContentView(content))
        doc_handling_presenter.start()
        
    def __styles(self):
        curses.start_color()
        curses.use_default_colors()  # ← esto es clave en muchas terminales

        if not curses.has_colors():
            raise RuntimeError("Tu terminal no soporta colores")

        curses.init_pair(1, -1, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_CYAN)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLUE)
