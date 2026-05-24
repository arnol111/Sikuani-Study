from src.models import FileDocument, KeyMapper
from src.interfaces.IDocHandlingPresenter import IDocHandlingPresenter
from src.interfaces.IContentView import IContentView
import logging
logging.basicConfig(filename="/tmp/sikuani_debug.log", level=logging.DEBUG)

class Doc_HandlingPresenter(IDocHandlingPresenter):
    def __init__(self, document: FileDocument, win: IContentView):
        self.doc = document
        self.win = win

    def start(self) -> None:
        while True:
            key_event = self.win.get_input()
            logging.debug(f"key_event={key_event}, key_event.key={key_event.key}")
            if key_event.key == KeyMapper.PRINTABLE:
                if key_event.char == 'q':
                    break
                self.__write_character(key_event.char)
            if key_event.key == KeyMapper.ENTER:
                self.__new_line()
            if key_event.key == KeyMapper.BACKSPACE:
                self.__remove_character()

    def __write_character(self, k: str) -> None:
        # pressedKey = chr(k)
        row = self.doc.lines[self.doc.pos_y]
        row = row[: self.doc.pos_x] + k + row[self.doc.pos_x :]
        self.doc.lines[self.doc.pos_y] = row
        self.win.render_ch(pos_x=self.doc.pos_x, pos_y=self.doc.pos_y, pressedKey=k)
        self.doc.pos_x += 1
        # Call terminal contetview
        

    def __new_line(self):
        row = self.doc.lines[self.doc.pos_y]
        before = row[: self.doc.pos_x]
        after = row[self.doc.pos_x :]
        self.doc.lines[self.doc.pos_y] = before
        self.doc.lines.insert(self.doc.pos_y + 1, after)
        self.doc.pos_y += 1
        self.doc.pos_x = 0
        # Call terminal ContentView
        self.win.render_new_line(pos_x=self.doc.pos_x, pos_y=self.doc.pos_y)
        

    def __remove_character(self) -> None:
        
        ## To do Fix bug when removing an entire line.
        if self.doc.pos_x > 0:
            row = self.doc.lines[self.doc.pos_y]
            self.doc.lines[self.doc.pos_y] = row[: self.doc.pos_x - 1] + row[self.doc.pos_x :]
            self.win.render_remove_ch(pos_x=self.doc.pos_x, pos_y=self.doc.pos_y)
            self.doc.pos_x -= 1
            # Call terminal ContentView
            

        if self.doc.pos_x == 0 and self.doc.pos_y > 0:
            prev = self.doc.lines[self.doc.pos_y - 1]
            last_location = len(prev.strip())
            self.doc.pos_y -= 1
            self.doc.pos_x = last_location
            ## Call terminal ContentView
            self.win.render_remove_ch(pos_y=self.doc.pos_y, pos_x=self.doc.pos_x)

    def __insert_text(self):
        pass
