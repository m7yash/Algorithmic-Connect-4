import random

import CheckWin
from CheckWin import *


class Simulate:
    simb = []  # should be filled by all 0s
    for i in range(0, 6):  # 6 rows
        x = []
        for j in range(0, 7):  # 7 columns
            x.append(0)
        simb.append(x)

    colc = []
    tot = 0

    def __init__(self, arr):  # takes in 2d array of integer colors
        self.colc = [0] * 7
        for i in range(0, 7):
            self.colc[i] = 0
        for r in range(0, 6):
            for c in range(0, 7):
                self.simb[r][c] = 0
        for r in range(0, 6):
            for c in range(0, 7):
                self.simb[r][c] = arr[r][c]
                if self.simb[r][c] != 0:
                    self.colc[c] = self.colc[c] + 1
                    self.tot = self.tot + 1

    def get_val(self):
        color = 1  # start with red
        while self.tot < 42:
            c = self.get_rand()
            if self.colc[c] < 6:
                self.simb[5 - self.colc[c]][c] = color
                if CheckWin.four_in_a_row_int_board(5 - self.colc[c], c, self.simb):
                    if color == 1:
                        return -1
                    if color == 2:
                        return 1
                self.colc[c] = self.colc[c] + 1
                if color == 1:
                    color = 2
                else:
                    color = 1
                self.tot = self.tot + 1
        return 0

    def get_rand(self):
        return random.randint(0, 6)  # random integer from 0 to 6
