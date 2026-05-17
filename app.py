import curses
from src.presenters import DocumentHandling
from src.presenters.Window import Window

def main(stdscr):

    stdscr.clear()
    stdscr.refresh()

    doc_handler = DocumentHandling(win=None, file_path="")
    window = Window(stdscr, doc_handler)
    window.start()

if __name__ == "__main__":

    curses.wrapper(main)