from pip._vendor.distlib.compat import raw_input
from termcolor import colored
import matplotlib.pyplot as plt

import Hard
from Hard import *


class Main:
    board = []
    for i in range(0, 6):  # 6 rows
        x = []
        for j in range(0, 7):  # 7 columns
            x.append(Cell())
        board.append(x)

    mp_games = 1
    mp_draws = 0
    gameIsOver = False
    allMoves = []

    red_just_won = False
    yellow_just_won = False
    draw_just_happened = False
    stop_the_print_for_draw = False

    a_was_selected = False

    humanPoints = 0
    computerPoints = 0

    level = 1000

    def __init__(self):
        print(colored("Welcome to Yash's Connect 4 Game!", 'blue'))
        print(colored(
            "Choose the difficulty! Type 'e' for easy, 'm' for medium, or 'h' for hard! Or, type 'a' for automated move!",
            'blue'))
        lev = raw_input("Level: ")

        if lev == "e":
            print(colored("You selected easy!", 'magenta'))
            self.level = 10
        elif lev == "m":
            print(colored("You selected medium!", 'magenta'))
            self.level = 50
        elif lev == "h":
            print(colored("You selected hard!", 'magenta'))
            self.level = 1000
        elif lev == "a":
            self.a_was_selected = True

            num_comp_vs_comp = raw_input("How many times should the computer play itself? ")  # check for non-int values

            if num_comp_vs_comp.isdigit() and int(num_comp_vs_comp) > 0:
                print(colored("The computer will play " + num_comp_vs_comp + " games.", 'blue'))
            else:
                print(colored("You did not choose a positive number. The number of games is set to 7 by default.",
                              'magenta'))
                num_comp_vs_comp = 7

            automated_difficulty = raw_input(
                "Type the number of simulations the computers should do for their moves. Your number must be between 1 and 1000. ")

            if automated_difficulty.isdigit() and 1 <= int(automated_difficulty) <= 1000:
                print(colored("The number of simulations will be " + automated_difficulty + ".", 'blue'))
                self.level = int(automated_difficulty)
            else:
                print(colored(
                    "You did not choose a number in the range 1 to 10000. The number of simulations is set to 100 by default.",
                    'blue'))
                self.level = 100

            num_red_wins = 0
            num_yellow_wins = 0
            num_total_games = 0

            for g in range(0, int(num_comp_vs_comp)):
                print(colored("----------------------------------------------", 'cyan'))
                print(colored("Game " + str(g + 1), 'cyan'))
                for i in range(0, 50):
                    r_move = self.c_red_move()
                    if self.red_just_won:
                        print(
                            colored("The red computer dropped a dot in column " + str(r_move + 1) + ".", 'magenta'))
                        self.generate_board()
                        self.other_reset_board()
                        print(colored("Red Computer Won!", 'blue'))
                        num_red_wins = num_red_wins + 1
                        self.other_reset_board()
                        self.red_just_won = False
                        num_total_games = num_total_games + 1
                        break

                    y_move = self.c_yellow_move()

                    if self.yellow_just_won:
                        print(
                            colored("The red computer dropped a dot in column " + str(r_move + 1) + ".", 'magenta'))
                        print(colored("The yellow computer dropped a dot in column " + str(y_move + 1) + ".",
                                      'magenta'))
                        self.generate_board()
                        self.other_reset_board()
                        print(colored("Yellow Computer Won!", 'blue'))
                        num_yellow_wins = num_yellow_wins + 1
                        self.other_reset_board()
                        self.yellow_just_won = False
                        num_total_games = num_total_games + 1
                        break

                    if self.draw_just_happened:
                        print(
                            colored("The red computer dropped a dot in column " + str(r_move + 1) + ".", 'magenta'))
                        print(colored("The yellow computer dropped a dot in column " + str(y_move + 1) + ".",
                                      'magenta'))
                        self.generate_board()
                        self.other_reset_board()
                        self.stop_the_print_for_draw = True
                        print(colored("Draw!", 'blue'))
                        self.draw_just_happened = False
                        num_total_games = num_total_games + 1
                        break

                    print(
                        colored("The red computer dropped a dot in column " + str(r_move + 1) + ".", 'magenta'))
                    if not self.red_just_won:
                        print(colored("The yellow computer dropped a dot in column " + str(y_move + 1) + ".",
                                      'magenta'))
                    if not self.stop_the_print_for_draw:
                        self.generate_board()
                    self.stop_the_print_for_draw = False
            print(colored("Red", 'red') + " won: " + str(num_red_wins) + " games.")
            print(colored("Red", 'red') + " won about: " + str(
                round(num_red_wins / num_total_games * 100, 2)) + "% of games.")
            print(colored("Yellow", 'yellow') + " won: " + str(num_yellow_wins) + " games.")
            print(colored("Yellow", 'yellow') + " won about: " + str(
                round(num_yellow_wins / num_total_games * 100, 2)) + "% of games.")

            num_drawn_games = num_total_games - (num_red_wins + num_yellow_wins)

            print("Drawn Games: " + str(num_drawn_games))
            print("Total Games: " + str(num_total_games))

            res = raw_input("Do you want to see the results graph? Type 'y' or 'n': ")

            if res == "y":
                names = ['Red Wins', 'Yellow Wins', 'Drawn Games']
                values = [num_red_wins, num_yellow_wins, num_drawn_games]

                plt.subplot(131)
                plt.bar(names, values, width=0.5, bottom=None, align='center', data=None,
                        color=('red', 'yellow', 'blue'))
                plt.suptitle('Game Summary: ' + str(num_comp_vs_comp) + " Games, " + str(
                    automated_difficulty) + " Simulations per Move.")
                plt.ylabel('Occurrences')
                plt.xlabel('Result')
                print(colored("Graph generated.", 'magenta'))
                plt.show()
            elif res == "n":
                print(colored("Graph not generated.", 'magenta'))
            else:
                print(colored("You did not type 'y' or 'n'. Graph not generated by default.", 'magenta'))

            fin = raw_input("Type r to replay the game or any other character to stop the game: ")

            if fin == "r":
                Main()
            else:
                print(colored("Game terminated.", 'magenta'))
                exit()
        else:
            print(colored("You did not choose 'e', 'm', 'h', or 'a'. The level is set to easy by default.", 'magenta'))
            self.level = 10

        if not self.a_was_selected:
            self.generate_board()
            print(
                colored("Your color will be ", 'blue') + colored("red", 'red') + colored(
                    ". The computer's color will be ",
                    'blue') + colored("yellow",
                                      'yellow') + colored(
                    ".", 'blue'))

            print(
                colored("Your last move will be represented by an ", 'blue') + colored("𝗼", 'red') + colored(
                    ". Your previous moves will be represented by an ",
                    'blue') + colored("𝗈",
                                      'red') + colored(
                    ".", 'blue'))

            print(
                colored("The computer's last move will be represented by an ", 'blue') + colored("𝗼",
                                                                                                 'yellow') + colored(
                    ". The computer's previous move will be represented by an ",
                    'blue') + colored("𝗈",
                                      'yellow') + colored(
                    ".", 'blue'))

            print(colored("----------------------------------------------", 'cyan'))
            print(colored("Game " + str(self.mp_games), 'cyan'))

            for r in range(0, 1000):
                g = raw_input(
                    "Type a column number to drop a dot in, 'u' to undo, 'r' to reset, 'p' to see points, 'f' to forfeit, or 's' to stop the game: ")
                if g == "u":
                    self.undo_move()
                elif g == "r":
                    if self.reset_board():
                        print((colored("Board reset.", 'magenta')))
                elif g == "p":
                    print(colored("Your Points: ", 'blue') + str(self.humanPoints))
                    print(colored("Computer's Points: ", 'blue') + str(self.computerPoints))
                    print(colored("Draws: ", 'blue') + str(self.mp_draws))
                elif g == "f":
                    print(colored("Game forfeited.", 'magenta'))
                    if not self.board_is_empty():
                        self.reset_board()
                    self.computer_point_increment()
                elif g == "s":
                    print(colored("Your Points: ", 'blue') + str(self.humanPoints))
                    print(colored("Computer's Points: ", 'blue') + str(self.computerPoints))
                    print(colored("Draws: ", 'blue') + str(self.mp_draws))

                    res = raw_input("Do you want to see the results graph? Type 'y' or 'n': ")

                    if res == "y":
                        names = ['Your Wins', 'Computer Wins', 'Drawn Games']
                        values = [self.humanPoints, self.computerPoints, self.mp_draws]

                        plt.subplot(131)
                        plt.bar(names, values, width=0.5, bottom=None, align='center', data=None,
                                color=('red', 'yellow', 'blue'))
                        plt.suptitle('Game Summary: ' + str(self.mp_games) + " Games, " + " Human vs Computer.")
                        plt.ylabel('Occurrences')
                        plt.xlabel('Result')
                        print(colored("Graph generated.", 'magenta'))
                        plt.show()
                    elif res == "n":
                        print(colored("Graph not generated.", 'magenta'))
                    else:
                        print(colored("You did not type 'y' or 'n'. Graph not generated by default.", 'magenta'))

                    print(colored("Game terminated.", 'magenta'))
                    exit()
                elif g.isdigit():
                    if 1 <= int(g) <= 7:
                        if self.p_move(int(g) - 1):  # if the player's move worked and was not a winning move
                            print(colored("You dropped a dot in column " + g + ".", 'magenta'))
                            print(colored("The computer dropped a dot in column " + str(self.c_move() + 1) + ".",
                                          'magenta'))
                    else:
                        print(colored("The column number must be between 1 and 7. Try again!", 'magenta'))
                else:
                    print(colored("'" + g + "'" + " is not a recognized command.", 'magenta'))
                self.generate_board()
            self.generate_board()

    def generate_board(self):
        print(colored("1  2  3  4  5  6  7", 'blue'))

        computer_last_row = 10
        computer_last_col = 10

        human_last_row = 10
        human_last_col = 10
        if len(self.allMoves) > 0:
            computer_last_row = self.get_row(len(self.allMoves) - 1)
            computer_last_col = self.get_col(len(self.allMoves) - 1)

            human_last_row = self.get_row(len(self.allMoves) - 2)
            human_last_col = self.get_col(len(self.allMoves) - 2)

        for i in range(0, 6):
            for j in range(0, 7):
                s = self.board[i][j].get_color_string()
                l = self.board[i][j].get_color_long()
                if i == computer_last_row and j == computer_last_col:
                    s = "𝗼"
                if i == human_last_row and j == human_last_col:
                    s = "𝗼"
                print(colored(str(s), l) + " ", end=' ')
            print()

    def p_move(self, col):
        if self.board[0][col].get_color() != 0:
            print(colored("That row is already filled up!", 'magenta'))
            return False
        put_in_bottom_row = True
        r = 0
        c = col
        for i in range(1, 6):
            if self.board[i][col].get_color() != 0:
                put_in_bottom_row = False
                r = i - 1
                self.allMoves.append(r * 10 + col)
                self.board[r][c].set_color(1)
                break
        if put_in_bottom_row:
            r = 5
            self.allMoves.append(r * 10 + col)
            self.board[r][col].set_color(1)
        if CheckWin.four_in_a_row(row=r, col=c, cell_board=self.board):
            self.human_point_increment()
            self.generate_board()
            print(colored("You Won! Keep it Up!", 'blue'))
            self.reset_board()
            self.mp_games = self.mp_games + 1
            print(colored("----------------------------------------------", 'cyan'))
            print(colored("Game " + str(self.mp_games), 'cyan'))
            return False

        return True

    def c_move(self):
        col = Hard.get_best_move(Hard(), self.board, self.level)
        r = 0
        c = col
        put_in_bottom_row = True
        for i in range(1, 6):  # rows 1 to 5
            if self.board[i][col].get_color() != 0:
                put_in_bottom_row = False
                r = i - 1
                self.allMoves.append(r * 10 + col)
                self.board[r][c].set_color(2)
                break
        if put_in_bottom_row:
            r = 5
            self.allMoves.append(r * 10 + col)
            self.board[r][c].set_color(2)

        check_if_draw = True

        if CheckWin.four_in_a_row(r, c, self.board):
            check_if_draw = False
            self.computer_point_increment()
            self.generate_board()
            print(colored("You lost! Try again!", 'blue'))
            self.reset_board()
            self.mp_games = self.mp_games + 1
            print(colored("----------------------------------------------", 'cyan'))
            print(colored("Game " + str(self.mp_games), 'cyan'))

        if len(self.allMoves) == 42 and check_if_draw:
            self.generate_board()
            print(colored("Draw!", 'blue'))
            self.mp_draws = self.mp_draws + 1
            self.reset_board()
            self.mp_games = self.mp_games + 1
            print(colored("----------------------------------------------", 'cyan'))
            print(colored("Game " + str(self.mp_games), 'cyan'))

        return col

    def c_red_move(self):
        col = Hard.get_best_move(Hard(), self.board, self.level)
        r = 0
        c = col
        put_in_bottom_row = True
        for i in range(1, 6):  # rows 1 to 5
            if self.board[i][col].get_color() != 0:
                put_in_bottom_row = False
                r = i - 1
                self.allMoves.append(r * 10 + col)
                self.board[r][c].set_color(1)
                break
        if put_in_bottom_row:
            r = 5
            self.allMoves.append(r * 10 + col)
            self.board[r][c].set_color(1)

        if CheckWin.four_in_a_row(r, c, self.board):
            self.red_just_won = True

        return col

    def c_yellow_move(self):
        col = Hard.get_best_move(Hard(), self.board, self.level)
        r = 0
        c = col
        put_in_bottom_row = True
        for i in range(1, 6):  # rows 1 to 5
            if self.board[i][col].get_color() != 0:
                put_in_bottom_row = False
                r = i - 1
                self.allMoves.append(r * 10 + col)
                self.board[r][c].set_color(2)
                break
        if put_in_bottom_row:
            r = 5
            self.allMoves.append(r * 10 + col)
            self.board[r][c].set_color(2)

        check_if_draw = True

        if CheckWin.four_in_a_row(r, c, self.board):
            check_if_draw = False
            self.yellow_just_won = True

        if len(self.allMoves) == 42 and check_if_draw:
            self.draw_just_happened = True

        return col

    def board_is_empty(self):
        board_is_empty = True
        for i in range(0, 6):
            for j in range(0, 7):
                if self.board[i][j].get_color() != 0:
                    board_is_empty = False
                    break
        return board_is_empty

    def reset_board(self):
        if self.board_is_empty():
            print(colored("The board is already empty!", 'blue'))
            return False

        for i in range(0, 6):
            for j in range(0, 7):
                self.board[i][j].set_color(0)

        self.allMoves.clear()

    def other_reset_board(self):
        for i in range(0, 6):
            for j in range(0, 7):
                self.board[i][j].set_color(0)

        self.allMoves.clear()

    def undo_move(self):
        if self.board_is_empty():
            print(colored("There is nothing to undo!", 'blue'))
            return False
        print(colored("Move undone.", 'magenta'))
        computer_last_row = self.get_row(len(self.allMoves) - 1)
        computer_last_col = self.get_col(len(self.allMoves) - 1)

        human_last_row = self.get_row(len(self.allMoves) - 2)
        human_last_col = self.get_col(len(self.allMoves) - 2)

        self.board[computer_last_row][computer_last_col].set_color(0)
        self.board[human_last_row][human_last_col].set_color(0)

        self.allMoves.remove(computer_last_row * 10 + computer_last_col)  # remove computer's last move
        self.allMoves.remove(human_last_row * 10 + human_last_col)  # undo human's last move

        return True

    def computer_point_increment(self):
        self.computerPoints = self.computerPoints + 1

    def human_point_increment(self):
        self.humanPoints = self.humanPoints + 1

    def get_row(self, index):
        return int(self.allMoves[index] / 10)

    def get_col(self, index):
        return int(self.allMoves[index] % 10)


Main()
