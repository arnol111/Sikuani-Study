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
        curses.raw()
        self.__styles()
        win = self.stdscr
        #win.bkgd(" ", curses.color_pair(1))
        high, width = win.getmaxyx()

        # Layout Windows
        title_bar = curses.newwin(1, width, 0, 0)
        content = curses.newwin(high - 2, width, 1, 0)
        footer = curses.newwin(1, width, high - 1, 0)

        content.bkgd(" ", curses.color_pair(1))

        # Validar depenencias de inyecciones
        FooterView(footer)
        TittleBarView(title_bar)

        # Modelo
        service = DocumentServices()
        document = service.load(self.file_path) 
        
        content.keypad(True)
        content.refresh()
        doc_handling_presenter = Doc_HandlingPresenter(document, ContentView(content), service)
        doc_handling_presenter.start()
        
    def __styles(self):
        curses.start_color()
        curses.use_default_colors()  # ← esto es clave en muchas terminales

        if not curses.has_colors():
            raise RuntimeError("Tu terminal no soporta colores")

        CP_NORMAL      = 1   # fg: #F8F8F2  bg: #272822
        CP_CURSOR_LINE = 2   # fg: #F8F8F2  bg: #3E3D32
        CP_STATUS      = 3   # fg: #75715E  bg: #1E1F1C
        CP_SIDEBAR     = 5   # fg: #A6E22E  bg: #1E1F1C  (Monokai green)
        CP_TITLE       = 6   # fg: #F92672  bg: #1E1F1C  (Monokai pink/red)


        BG_MAIN   = 235   # #272822
        BG_PANEL  = 234   # #1E1F1C
        BG_LINE   = 236   # #3E3D32
        FG_NORMAL = 253   # #F8F8F2
        FG_STATUS = 242   # #75715E
        FG_GREEN  = 148   # #A6E22E
        FG_PINK   = 197   # #F92672

        curses.init_pair(CP_NORMAL,      FG_NORMAL, BG_MAIN)
        curses.init_pair(CP_CURSOR_LINE, FG_NORMAL, BG_LINE)
        curses.init_pair(CP_STATUS,      FG_STATUS, BG_PANEL)
        curses.init_pair(CP_SIDEBAR,     FG_GREEN,  BG_PANEL)
        curses.init_pair(CP_TITLE,       FG_PINK,   BG_PANEL)
        
        #curses.init_pair(1, -1, curses.COLOR_CYAN)
        #curses.init_pair(2, curses.COLOR_RED, curses.COLOR_CYAN)
        #curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLUE)
