class ContainerView:
    def __init__(self, window):
        self.window = window

    def render(self, pos_x, pos_y, lines: list[str]):
        self.window.clear()
        for i, line in enumerate(lines):
            self.window.addstr(i, 0, line)
        self.window.move(pos_y, pos_x)
        self.refresh()

    def get_input(self) -> int:
        return self.window.getch()
