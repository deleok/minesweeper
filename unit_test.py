"""
Qibai Zhu

This unit test will also write the mine hints output to the minesweeper_output.txt file.

The shortcoming is that field number is not in order, i.e. Field #num, maybe you will
see the Field #1 all the time.
"""


import unittest
from process_input import ProcessInput


class ProcessInputUnitTest(unittest.TestCase):

    def test_minimum_with_one_row_one_col_zero_mine(self):
        ps = ProcessInput(None)
        # with open("minesweeper_output.txt", "w"):
        #     pass

        ps.process_content(['1 1', '.', '0 0'])
        test_mine_hints = ps.get_mine_hints()
        actual_mine_hints = [['0']]
        self.assertListEqual(actual_mine_hints, test_mine_hints)

    def test_minimum_with_one_row_one_col_all_mines(self):
        ps = ProcessInput(None)
        # with open("minesweeper_output.txt", "w"):
        #     pass

        ps.process_content(['1 1', '*', '0 0'])
        test_mine_hints = ps.get_mine_hints()
        actual_mine_hints = [['*']]
        self.assertListEqual(actual_mine_hints, test_mine_hints)

    def test_maximum_with_100_row_100_col_zero_mine(self):
        ps = ProcessInput(None)
        # with open("minesweeper_output.txt", "w"):
        #     pass

        # input content list
        input_one_line = '.' * 100
        input_list = ['100 100']
        for _ in range(100):
            input_list.append(input_one_line)
        input_list.append('0 0')
        ps.process_content(input_list)
        test_mine_hints = ps.get_mine_hints()

        # output hints
        actual_mine_hints = []

        for _ in range(100):
            actual_mine_hints.append(['0' for _ in range(100)])

        self.assertListEqual(actual_mine_hints, test_mine_hints)

    def test_maximum_with_100_row_100_col_all_mines(self):
        ps = ProcessInput(None)
        # with open("minesweeper_output.txt", "w"):
        #     pass

        # input content list
        input_one_line = '*' * 100
        input_list = ['100 100']
        for line in range(100):
            input_list.append(input_one_line)
        input_list.append('0 0')
        ps.process_content(input_list)
        test_mine_hints = ps.get_mine_hints()

        # output hints
        actual_mine_hints = []

        for _ in range(100):
            actual_mine_hints.append(['*' for _ in range(100)])

        self.assertListEqual(actual_mine_hints, test_mine_hints)

    def test_one_row_100_col_zero_mine(self):
        ps = ProcessInput(None)
        # with open("minesweeper_output.txt", "w"):
        #     pass

        # input content list
        input_one_line = '.' * 100
        input_list = ['1 100']
        input_list.append(input_one_line)
        input_list.append('0 0')
        ps.process_content(input_list)
        test_mine_hints = ps.get_mine_hints()

        # output hints
        actual_mine_hints = [['0']]

        for _ in range(99):
            actual_mine_hints[0].append('0')

        self.assertListEqual(actual_mine_hints, test_mine_hints)

    def test_100_row_one_col_all_mines(self):
        ps = ProcessInput(None)
        # with open("minesweeper_output.txt", "w"):
        #     pass

        # input content list
        input_one_line = '*'
        input_list = ['100 1']
        for _ in range(100):
            input_list.append(input_one_line)
        input_list.append('0 0')
        ps.process_content(input_list)
        test_mine_hints = ps.get_mine_hints()

        # output hints
        actual_mine_hints = []

        for _ in range(100):
            actual_mine_hints.append(['*'])
        self.assertListEqual(actual_mine_hints, test_mine_hints)

    def test_3_row_2_col_2_mines(self):
        ps = ProcessInput(None)
        # with open("minesweeper_output.txt", "w"):
        #     pass

        ps.process_content(['3 2', '*.', '..', '.*', '0 0'])
        test_mine_hints = ps.get_mine_hints()

        actual_mine_hints = [['*', '1'], ['2', '2'], ['1', '*']]
        self.assertListEqual(actual_mine_hints, test_mine_hints)


if __name__ == '__main__':
    unittest.main()
