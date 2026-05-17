import logging
from io import BufferedIOBase
import os
from src.interfaces import IDocumentHandling
import curses


class DocumentHandling(IDocumentHandling):
    def __init__(self, win, file_path: str):
        self.start_y = 0
        self.start_x = 0
        self.win = win
        self.array_text = []
        self.file_document: BufferedIOBase | None = None
        if file_path:
            self.load_document(file_path)
        #logging.basicConfig(filename="/tmp/debug.log", level=logging.DEBUG)

    def write_character(self):
        k = 0
        self.array_text = [""]
        self.start_y = 0
        self.start_x = 0
        if self.file_document:
            self.array_text = self.file_document.readlines()

        while k != ord("q"):

            k = self.win.getch()
            if k != 0:
                pressedKey = chr(k)

                #logging.debug(f"star_y={self.start_y} star_x={self.start_x} and k={k}")

                if 32 <= k <= 126:
                    row = self.array_text[self.start_y]
                    row = row[: self.start_x] + pressedKey + row[self.start_x :]
                    self.array_text[self.start_y] = row
                    self.win.addstr(self.start_y, self.start_x, pressedKey, curses.color_pair(2))
                    self.start_x += 1
                    self.win.move(self.start_y, self.start_x)

                elif k == 10 or k == ord("\n"):
                    row = self.array_text[self.start_y]
                    before = row[: self.start_x]
                    after = row[self.start_x :]
                    self.array_text[self.start_y] = before
                    self.array_text.insert(self.start_y + 1, after)
                    self.start_y += 1
                    self.start_x = 0
                    self.win.move(self.start_y, self.start_x)

                elif k == curses.KEY_BACKSPACE or k == 127:
                    self.remove_character()

            self.win.refresh()

    def remove_character(self):
        """Delete the character before the cursor.
        Returns:
            int: 1 if a character was removed,
                -1 if an entire line was removed,
                0 if nothing was removed.
        """
        if self.start_x > 0:
            row = self.array_text[self.start_y]
            self.array_text[self.start_y] = (row[: self.start_x - 1] + row[self.start_x :])
            self.start_x -= 1
            self.win.delch(self.start_y, self.start_x)
            return 1

        if self.start_x == 0 and self.start_y > 0:
            prev = self.array_text[self.start_y - 1]
            last_location = len(prev.strip())
            self.win.deleteln()
            self.win.refresh()
            self.start_y -= 1
            self.start_x = last_location
            self.win.move(self.start_y, self.start_x)
            return -1
        return 0

    def save_document(self, document):
        pass

    def load_document(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} is missing!")
        self.file_document = open(file_path, "w+b", encoding="utf-8")

    def insert_text(self, document):
        pass
