"""
Kishan Vekaria

Terminal code to run code:
python mineSweeper.py < minesweeper_input.txt > minesweeper_output.txt
first .py file is the actual code
second .txt file indicates where the first file will read input from
third .txt file indicates where the output of the first file will go
"""


def split(word):
    """Returns a string as individual characters"""
    return [char for char in word]


def read_input():
    """Reads from input file to create minefields"""
    condition = True
    list_of_games = []  # Holds all minefield games as separate arrays in an array (2d array)
    while condition:
        game_board_size = input()  # First line in input file determines size of game board
        row_and_col = game_board_size.split(" ")  # splitting input using the "space" in between the two numbers
        number_of_rows = int(row_and_col[0])  # first number determines number of rows
        number_of_cols = int(row_and_col[1])  # second number determines number of columns
        if number_of_cols != 0 and number_of_rows != 0:  # Last line in file will always be "0 0"
            input_board = create_game_board(number_of_cols, number_of_rows)  # creates game board from input
            list_of_games.append(input_board)  # adds game board to list of minefields
        else:
            condition = False
    return list_of_games  # returns all game boards from input


def create_game_board(number_of_cols, number_of_rows):
    """For each minefield from input file, a game board (2d array is created)"""
    # Create 2d array
    my_array = []
    for i in range(number_of_rows):
        row = []
        list_of_input = input()
        split(list_of_input)
        for j in list_of_input:
            row.append(j)
        my_array.append(row)
    return my_array


def create_solution():
    """
    Creates blank game boards (2d array) filled with zeros. Then compares with game board and creates solution
    :return: Game number and solution to minesweeper
    """
    minesweeper_boards = read_input()  # returns input_board ( 2d array of input on a single line)
    game_counter = 1  # keeps track of 2d arrays for output file
    for game_board in minesweeper_boards:
        print("Field #" + str(game_counter) + ":")
        game_counter += 1
        row_counter = 0
        for row in game_board:
            col_counter = 0
            row_counter += 1
            for item in row:
                col_counter += 1
        rows, cols = (row_counter, col_counter)  # size of minesweeper array
        blank_game_board = []
        for i in range(rows):  # creates blank 2d array filled with zeros
            row = []
            for j in range(cols):
                row.append(0)
            blank_game_board.append(row)
        row_max = rows + 1  # row max size
        col_max = cols + 1  # column max size
        for row in range(rows):
            for col in range(cols):
                if game_board[row][col] == "*":  # if item in 2d array is a mine, increase all adjacent numbers by 1
                    blank_game_board[row][col] = "*"  # copies mine(*) to blank minefield
                    # Right
                    if col + 1 < col_max:
                        try:
                            if game_board[row][col + 1] != "*":
                                blank_game_board[row][col + 1] += 1
                        except:
                            pass

                    # # bottom right
                    if row < row_max and col < col_max:
                        try:
                            if game_board[row + 1][col + 1] != "*":
                                blank_game_board[row + 1][col + 1] += 1
                        except:
                            pass

                    # # bottom
                    if row < row_max:
                        try:
                            if game_board[row + 1][col] != "*":
                                blank_game_board[row + 1][col] += 1
                        except:
                            pass

                    # # bottom left
                    if row + 1 >= row_max or col - 1 != -1:
                        try:
                            if game_board[row + 1][col - 1] != "*":
                                blank_game_board[row + 1][col - 1] += 1
                        except:
                            pass

                    # # left
                    if col - 1 != -1:
                        try:
                            if game_board[row][col - 1] != "*":
                                blank_game_board[row][col - 1] += 1
                        except:
                            pass

                    # # top left
                    if row - 1 != -1 and col - 1 != -1:
                        try:
                            if game_board[row - 1][col - 1] != "*":
                                blank_game_board[row - 1][col - 1] += 1
                        except:
                            pass
                    # # top
                    if row - 1 != -1:
                        try:
                            if game_board[row - 1][col] != "*":
                                blank_game_board[row - 1][col] += 1
                        except:
                            pass

                    # # top right
                    if row - 1 != -1 and col + 1 < col_max:
                        try:
                            if game_board[row - 1][col + 1] != "*":
                                blank_game_board[row - 1][col + 1] += 1
                        except:
                            pass

        for game in blank_game_board:  # prints minefields for output file
            for row in game:
                print(row, end="")
            print()
        print()


if __name__ == "__main__":
    create_solution()

# Sample Input data
# 4 4
# *..*
# .*..
# ...*
# *...
# 4 4
# *...
# ....
# .*..
# ....
# 3 5
# **...
# .....
# .*...
# 0 0
