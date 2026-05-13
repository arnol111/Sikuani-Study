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
        barra = win.derwin(1, width,0, 0)
        barra.bkgd(' ', curses.color_pair(3))
        #barra.clear()
        barra.addstr(0, 0, "BARRA DE TAREAS",curses.color_pair(3))
        
        barra.refresh()  
        win.move(1,0)         
        document = ""
        self.doc_handler.write_character()

    