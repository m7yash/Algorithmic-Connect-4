class Cell:
    colorOfCell = 0  # white

    def __init__(self):
        self.colorOfCell = 0  # white

    def get_color(self):
        return self.colorOfCell

    def get_color_string(self):
        if self.colorOfCell == 0:
            return "."
        elif self.colorOfCell == 1:
            return "𝗈"
        else:
            return "𝗈"

    def get_color_long(self):
        if self.colorOfCell == 0:
            return 'white'
        elif self.colorOfCell == 1:
            return 'red'
        else:
            return 'yellow'

    def set_color(self, c):  # c = 0 is white, c = 1 is red, c = 2 is yellow
        self.colorOfCell = c
