"""
Kara de Leon's Individual Solution

This program creates fields for the game Minesweeper.
Given mindsweeper_input.txt, fields are created with hints in mindsweeper_output.txt.

"""

def process_content(lines):
    '''
    :param lines: the file content
    :return: a list of boards
    '''
    boards = []
    last_line_index = len(lines) - 1
    line_index = 0
    while line_index <= last_line_index:
        dimension = lines[line_index].split(" ")
        row_count = int(dimension[0])
        col_count = int(dimension[1])

        # base case when we reach the line
        # that has the dimension 0 0
        if row_count == 0 and col_count == 0:
            return boards

        # initiate the empty mine board
        board = [[0 for _ in range(col_count)] for _ in range(row_count)]
        line_index = line_index + 1

        # read the next row count
        row_index = 0
        while row_index < row_count:

            col_index = 0
            while col_index < col_count:
                # read data into the board
                board[row_index][col_index] = lines[line_index][col_index]

                # increase the column index
                col_index = col_index + 1

            # increase the row index
            # to avoid infinite loop
            row_index = row_index + 1

            # increase the line index
            # to continue reading the board
            # at appropriate lines
            line_index = line_index + 1

        # finished putting data into a board
        # then simply add that board to the list of boards
        boards.append(board)

        # increase the line index
        #line_index = line_index + 1

    return boards

def provide_hint(board):
    '''
    :param board: the 2D-array
    :return: the 2D-array with hints
    '''
    row_count = len(board)
    col_count = len(board[0])

    # iterate over all cells in the board
    for row in range(row_count):
        for col in range(row_count):

            # simply do nothing
            if board[row][col] == '*':
                continue

            # start counting the mine around the cell
            # we only count the in-bound indexes
            count = 0

            # northwest (top left)
            if row-1 >= 0 and col-1 >= 0 and board[row-1][col-1] == '*':
                count = count + 1

            # north (top)
            if row - 1 >= 0 and board[row - 1][col] == '*':
                count = count + 1

            # northeast (top right)
            if row - 1 >= 0 and col + 1 < col_count and board[row - 1][col + 1] == '*':
                count = count + 1

            # west (left)
            if col - 1 >= 0 and board[row][col - 1] == '*':
                count = count + 1

            # east (right)
            if col + 1 < col_count and board[row][col + 1] == '*':
                count = count + 1

            # southwest (bottom left)
            if row + 1 < row_count and col - 1 >= 0 and board[row + 1][col - 1] == '*':
                count = count + 1

            # south (down)
            if row + 1 < row_count and board[row + 1][col] == '*':
                count = count + 1

            # southeast (bottom right)
            if row + 1 < row_count and col + 1 < col_count and board[row + 1][col + 1] == '*':
                count = count + 1

            # provide the hint number in the current cell
            board[row][col] = str(count)

def write_to_file(file, boards):
    '''
    :param file: file output
    :param boards: list of boards
    :return:
    '''
    board_index = 0
    board_total = len(boards)

    while board_index < board_total:

        file.write("Field #{}:\n".format(board_index + 1))
        row_count = len(boards[board_index])
        for row_index in range(row_count):
            file.write("{}\n".format(''.join(boards[board_index][row_index])))
        file.write("\n")

        # move to the next board
        board_index = board_index + 1

if __name__ == "__main__":
    # for requirements
    # boards = process_content(sys.stdin.readlines())

    # for debugging purpose
    file = open("minesweeper_input.txt", "r")
    boards = process_content(file.readlines())
    file.close()
    for board in boards:
        provide_hint(board)

    file = open("minesweeper_output.txt", "w")
    write_to_file(file, boards)
    file.close()