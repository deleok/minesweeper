"""
Qibai Zhu
"""


class MineSweeper:
    """
    MineSweeper class will initially generate an empty mine field, then through reading string from txt.file, it can
    create a mine field with mines "*" and safe spot "." ; Then it can draw the mine hints for each field spot by
    counting the at most 8 adjacent squares.
    """

    def __init__(self, row, col):
        """
        Generate a two-D dimensional array mine field with passed row and column
        :param row: passed row of minesweeper
        :param col: passed column of minesweeper
        """
        self.__row = row
        self.__col = col
        self.__field = []
        for _ in range(0, self.__row):
            self.__field.append(['' for _ in range(0, self.__col)])

    def get_field(self):
        """
        Get Mine field
        """
        return self.__field

    def create_mine_field(self, one_line_str, row):
        """
        Read one line string from text file, put each character of the string into the specific row of mine field
        :param one_line_str: one line string from the text file
        :param row: row of mine field
        """
        for col, value in enumerate(one_line_str):
            self.__field[row][col] = value

    def draw_field_hints(self):
        """
        Convert '.' into hints numbers in the mine field
        """
        for row in range(0, self.__row):
            for col in range(0, self.__col):
                if self.__field[row][col] == '*':
                    continue
                mines_num = self.count_mines_around_spot(row, col)
                self.__field[row][col] = str(mines_num)

    def print_field_hints(self):
        """
        Print the mine field with the number of mines
        """
        return '\n'.join(map(''.join, self.__field))

    def count_mines_around_spot(self, row, col):
        """
        For each spot in the mine field, count the number of mines adjacent to that spot, each spot
        has at most 8 adjacent squares.
        :param row: the row number of spot position
        :param col: the col number of spot position
        """
        count_mines = 0
        row_delta = [0, 0, -1, -1, -1, 1, 1, 1]
        col_delta = [-1, 1, -1, 0, 1, -1, 0, 1]
        for i in range(0, 8):
            new_row = row + row_delta[i]
            new_col = col + col_delta[i]

            if self.is_valid_spot(new_row, new_col):
                if self.__field[new_row][new_col] == '*':
                    count_mines += 1
        return count_mines

    def is_valid_spot(self, row, col):
        """
        Check whether the passed number (row, col) consist of valid spot in the field
        :param row: the row number of spot position
        :param col: the col number of spot position
        :return:
        """
        return 0 <= row < self.__row and 0 <= col < self.__col
