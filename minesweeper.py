class MineSweeper:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__field = []
        for _ in range(0, self.__row):
            self.__field.append(['' for _ in range(0, self.__col)])

    def get_field(self):
        return self.__field

    def create_mine_field(self, one_line_str, row):
        for col, value in enumerate(one_line_str):
            self.__field[row][col] = value

    def draw_field_hints(self):
        for row in range(0, self.__row):
            for col in range(0, self.__col):
                if self.__field[row][col] == '*':
                    continue
                mines_num = self.count_mines_around_spot(row, col)
                self.__field[row][col] = str(mines_num)

    def print_field_hints(self):
        return '\n'.join(map(''.join, self.__field))

    def count_mines_around_spot(self, row, col):
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
        return 0 <= row < self.__row and 0 <= col < self.__col
