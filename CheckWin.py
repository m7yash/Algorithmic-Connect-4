from Cell import *


def four_in_a_row_int_board(row, col, int_board):
    myCell = []
    for i in range(0, 6):  # 6 rows
        x = []
        for j in range(0, 7):  # 7 columns
            x.append(Cell())
        myCell.append(x)

    for i in range(0, 6):
        for j in range(0, 7):
            myCell[i][j].set_color(int_board[i][j])

    return four_in_a_row(row, col, myCell)


def four_in_a_row(row, col, cell_board):
    if vertical_four(row, col, cell_board) or horizontal_four(row, col,
                                                              cell_board) or diagonal_a_four(row,
                                                                                             col,
                                                                                             cell_board) or diagonal_b_four(
        row, col, cell_board):
        return True
    else:
        return False


def vertical_four(row, col, cell_board):
    color = cell_board[row][col].get_color()
    streak = 0
    max_streak = 0
    for i in range(0, 6):
        if cell_board[i][col].get_color() == color:
            streak = streak + 1
        else:
            streak = 0
        if streak > max_streak:
            max_streak = streak
    return max_streak >= 4


def horizontal_four(row, col, cell_board):
    color = cell_board[row][col].get_color()
    streak = 0
    max_streak = 0
    for j in range(0, 7):
        if cell_board[row][j].get_color() == color:
            streak = streak + 1
        else:
            streak = 0
        if streak > max_streak:
            max_streak = streak
    return max_streak >= 4


def diagonal_a_four(row, col, cell_board):
    color = cell_board[row][col].get_color()
    streak = 0
    max_streak = 0
    sr = 0
    sc = 0
    er = 0
    ec = 0
    if row - 3 >= 0 and col - 3 >= 0:
        sr = row - 3
        sc = col - 3
    else:
        minimum = row
        if col < row:
            minimum = col
        sr = row - minimum
        sc = col - minimum

    if row + 3 <= 5 and col + 3 <= 6:
        er = row + 3
        ec = col + 3
    else:
        minimum = 5 - row
        if 6 - col < 5 - row:
            minimum = 6 - col
        er = row + minimum
        ec = col + minimum
    i = sr
    j = sc
    while i <= er and j <= ec:
        if cell_board[i][j].get_color() == color:
            streak = streak + 1
        else:
            streak = 0
        if streak > max_streak:
            max_streak = streak

        i = i + 1
        j = j + 1
    return max_streak >= 4


def diagonal_b_four(row, col, cell_board):
    color = cell_board[row][col].get_color()
    streak = 0
    max_streak = 0
    sr = 0
    sc = 0
    er = 0
    ec = 0
    if row - 3 >= 0 and col + 3 <= 6:
        sr = row - 3
        sc = col + 3
    else:
        minimum = row
        if 6 - col < row:
            minimum = 6 - col
        sr = row - minimum
        sc = col + minimum

    if row + 3 <= 5 and col - 3 >= 0:
        er = row + 3
        ec = col - 3
    else:
        minimum = 5 - row
        if col < 5 - row:
            minimum = col
        er = row + minimum
        ec = col - minimum
    i = sr
    j = sc
    while i <= er and j >= ec:
        if cell_board[i][j].get_color() == color:
            streak = streak + 1
        else:
            streak = 0
        if streak > max_streak:
            max_streak = streak

        i = i + 1
        j = j - 1
    return max_streak >= 4
