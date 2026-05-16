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

    def write_character(self):

        k = 0
        self.start_y = 1
        self.start_x = 0
        actual_row = ""

        if self.file_document:
            self.array_text = self.file_document.readlines()

        while k != ord("q"):
            k = self.win.getch()

            if k != 0:
                height, width = self.win.getmaxyx()
                pressedKey = chr(k)

                if 32 <= k <= 126:
                    self.win.attron(curses.color_pair(2))
                    self.win.addstr(self.start_y, self.start_x, pressedKey)
                    actual_row += pressedKey
                    self.start_x += 1
                    self.win.move(self.start_y, self.start_x)

                if k == 10 or k == ord("\n"):
                    self.start_y += 1
                    self.start_x = 0
                    self.array_text.append(actual_row)
                    self.win.move(self.start_y, self.start_x)

                elif k == curses.KEY_BACKSPACE:
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
            self.start_x -= 1
            self.win.delch(self.start_y, self.start_x)
            return 1


        # Todo : Fix the error when remove a line
        if self.start_x == 0:
            if self.start_y > 1:
                self.start_y -= 1
                self.win.delch(self.start_y, self.start_x)
                self.start_x = len(self.array_text[self.start_y-1].strip())
                self.win.move(self.start_y, self.start_x)
                return -1

            else:
                self.win.delch(self.start_y, self.start_x)
                return 1
        return 0

    def save_document(self, document):
        pass

    def load_document(self, file_path: str):

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} is missing!")

        self.file_document = open(file_path, "w+b", encoding="utf-8")

    def insert_text(self, document):
        pass
