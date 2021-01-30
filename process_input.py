"""
Qibai Zhu

This ProcessInput program can read input from minesweeper_input.txt and
write output into minesweeper_output.txt
"""

from minesweeper import MineSweeper


class ProcessInput:

    def __init__(self, file_name):
        """
        Open file that want to be processed,read all lines of strings in the file, content will be stored in the list
        :param file_name: txt.file name
        """
        if file_name:
            with open(file_name) as f:
                self.__content_list = f.read().splitlines()
        self.__count_field = 0

    def get_content_list(self):
        """
        Get content list
        """
        return self.__content_list

    def get_row_and_col(self, number_str):
        """
        Parse the String into integer row and column
        :param number_str: string of row and column
        :return: row, column
        """

        field_size = [int(num) for num in number_str.split()]
        row = field_size[0]
        col = field_size[1]
        return row, col

    def process_content(self, content_list):
        """
        Process the content from minesweeper_input.txt file, generate minesweeper and draw the hints numbers,
        write the hints output into minesweeper_output.txt file
        """
        global mine_field
        line = 0

        while line < len(content_list):

            row, col = self.get_row_and_col(content_list[line])

            if row == 0 and col == 0:
                break

            self.__count_field += 1

            row_limit = line + row
            line += 1

            mine_field = MineSweeper(row, col)

            mine_field_row_line = 0
            while line <= row_limit:
                mine_field.create_mine_field(content_list[line], mine_field_row_line)
                mine_field_row_line += 1
                line += 1

            mine_field.draw_field_hints()
            # print the hints to minesweeper_output.txt file
            self.print_mine_hints_to_file()

    def get_mine_hints(self):
        return mine_field.get_field()

    def print_mine_hints_to_file(self):
        with open("minesweeper_output.txt", "a") as text_file:
            print("Field #{}:\n{}\n".format(self.__count_field, mine_field.print_field_hints()), file=text_file)


if __name__ == '__main__':
    ps = ProcessInput('minesweeper_input.txt')
    with open("minesweeper_output.txt", "w"):
        pass
    ps.process_content(ps.get_content_list())
