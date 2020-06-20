from Simulate import *


class Hard:
    mxval = -99999
    colval = [0] * 7  # list of 7 elements, all of which are 0
    colcolcol = [0] * 7
    total = 0
    bestcol = 0
    gg = []  # should be filled by all 0s
    for i in range(0, 6):  # 6 rows
        x = []
        for j in range(0, 7):  # 7 columns
            x.append(0)
        gg.append(x)

    def get_best_move(self, grid, game_lev):
        for r in range(0, 6):
            for c in range(0, 7):
                self.gg[r][c] = 0
                self.gg[r][c] = grid[r][c].get_color()
        self.bestcol = -1
        total = 0
        self.mxval = -99999
        for i in range(0, 7):
            self.colcolcol[i] = 0
            self.colval[i] = 0

        for r in range(0, 6):
            for c in range(0, 7):
                if self.gg[r][c] > 0:
                    self.colcolcol[c] = self.colcolcol[c] + 1
                    total = total + 1

        if total == -42:
            return -1

        for c in range(0, 7):
            if self.colcolcol[c] == 6:
                continue
            self.gg[5 - self.colcolcol[c]][c] = 2
            if CheckWin.four_in_a_row_int_board(5 - self.colcolcol[c], c, self.gg):
                return c
            for i in range(1, game_lev):  # Number of simulations
                nsim = Simulate(self.gg)
                self.colval[c] = self.colval[c] + nsim.get_val()
            self.gg[5 - self.colcolcol[c]][c] = 0

        for c in range(0, 7):
            if self.colcolcol[c] == 6:
                continue
            if self.colval[c] > self.mxval:
                self.bestcol = c
                self.mxval = self.colval[c]

        return self.bestcol
