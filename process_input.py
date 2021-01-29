from minesweeper import MineSweeper


class ProcessInput:
    def __init__(self, file_name):
        with open(file_name) as f:
            self.__content_list = f.read().splitlines()

    def get_content_list(self):
        return self.__content_list

    def get_row_and_col(self, number_str):
        field_size = [int(num) for num in number_str.split()]
        row = field_size[0]
        col = field_size[1]
        return row, col

    def process_content(self):
        global mine_field
        count_field = 0
        line = 0

        while line < len(self.__content_list):

            row, col = self.get_row_and_col(self.__content_list[line])

            if row == 0 and col == 0:
                break

            count_field += 1

            row_limit = line + row
            line += 1

            mine_field = MineSweeper(row, col)

            mine_field_row_line = 0
            while line <= row_limit:
                mine_field.create_mine_field(self.__content_list[line], mine_field_row_line)
                mine_field_row_line += 1
                line += 1

            mine_field.draw_field_hints()

            with open("minesweeper_output.txt", "a") as text_file:
                print("Field #{}:\n{}\n".format(count_field, mine_field.print_field_hints()), file=text_file)


if __name__ == '__main__':
    ps = ProcessInput('minesweeper_input.txt')
    with open("minesweeper_output.txt", "w"):
        pass
    ps.process_content()
