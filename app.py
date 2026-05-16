import curses
from src.presenters import DocumentHandling
from src.presenters.Window import Window

def main(stdscr):

    stdscr.clear()
    stdscr.refresh()
    curses.start_color()
    curses.use_default_colors()  # ← esto es clave en muchas terminales

    if not curses.has_colors():
        raise RuntimeError("Tu terminal no soporta colores")

    curses.init_pair(1, -1, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLUE)

    doc_handler = DocumentHandling(win=stdscr, file_path="")
    window = Window(stdscr, doc_handler)
    window.start()

if __name__ == "__main__":

    curses.wrapper(main)