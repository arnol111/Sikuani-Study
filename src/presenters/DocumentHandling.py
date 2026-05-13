from src.interfaces import IDocumentHandling
import curses


class DocumentHandling(IDocumentHandling):
    def __init__(self, win, document:str):
        self.start_y = 0
        self.start_x = 0
        self.win = win
        self.document = document
        
    def write_character(self):

        k = 0
        self.start_y = 1
        self.start_x = 0

        while k != ord("q"):
            k = self.win.getch()

            if k != 0:
                height, width = self.win.getmaxyx()
                pressedKey = chr(k)

                if 32 <= k <= 126:
                    self.win.attron(curses.color_pair(2))
                    self.win.addstr(self.start_y, self.start_x, pressedKey)
                    ##self.win.attroff(curses.color_pair(2))
                    self.start_x += 1
                    self.win.move(self.start_y, self.start_x)

                if k == 10 or k == ord("\n"):
                    self.start_y += 1
                    self.start_x = 0
                    self.win.move(self.start_y, self.start_x)

                elif k == curses.KEY_BACKSPACE:
                    self.remove_character()

            self.win.refresh()

    def remove_character(self):
        if self.start_x > 0:
            self.start_x -= 1
            self.win.delch(self.start_y, self.start_x)
            
            if self.start_x == 0:
                if self.start_y > 0:
                    self.start_y -= 1
                    self.win.delch(self.start_y, self.start_x)
                else:
                    self.win.delch(self.start_y, self.start_x)

    def save_document(self, document):
        pass

    def load_document(self, document):
        pass

    def insert_text(self, document):
        pass
