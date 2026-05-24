import curses
from src.presenters.Window import Window

def main(stdscr):

    stdscr.clear()
    stdscr.refresh()
    
    window = Window(stdscr, file_path="")
    window.start()

if __name__ == "__main__":

    curses.wrapper(main)