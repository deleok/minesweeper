import random


class GenerateField:

    def __init__(self):
        self.__row_size = random.randint(3, 5)
        self.__col_size = random.randint(2, 5)
        self.__mine_number = random.randint(2, self.__row_size * self.__col_size // 2)
        self.__field = []

        for _ in range(0, self.__row_size):
            self.__field.append(['' for _ in range(0, self.__col_size)])

    def get_row_size(self):
        return self.__row_size

    def get_col_size(self):
        return self.__col_size

    def place_mine(self):

        while self.__mine_number > 0:
            row = random.randint(0, self.__row_size - 1)
            col = random.randint(0, self.__col_size - 1)

            if self.__field[row][col] != '*':
                self.__field[row][col] = '*'
                self.__mine_number -= 1

    def draw_mine_field(self):
        for row in range(0, self.__row_size):
            for col in range(0, self.__col_size):
                if self.__field[row][col] != '*':
                    self.__field[row][col] = '.'

    def print_field(self):
        return self.__str__()

    def __str__(self):
        return '\n'.join(map(''.join, self.__field))


def generate_input(number_of_fields):
    while number_of_fields > 0:
        field = GenerateField()

        row_size = field.get_row_size()
        col_size = field.get_col_size()

        if row_size != 0 and col_size != 0:
            field.place_mine()
            field.draw_mine_field()
        with open("minesweeper_input.txt", "a") as text_file:
            print("{} {}\n{}".format(row_size, col_size, field.print_field()), file=text_file)

        number_of_fields -= 1

    with open("minesweeper_input.txt", "a") as text_file:
        print("0 0", file=text_file)


if __name__ == '__main__':
    with open("minesweeper_input.txt", "w"):
        pass
    generate_input(2)
