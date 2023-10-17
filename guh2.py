def initialize_board(num_rows=4, num_cols=4):  # Creates a blank board based on how tall and long the user wants
    board = []
    for i in range(num_rows):
        board.append([])
        for j in range(num_cols):
            board[i].append('-')
    return board


def print_board(board: list):
    board.reverse()
    for row in board:
        for col_val in row:
            print(col_val, end=' ')
        print()
    board.reverse()


def check_if_winner(board: list, col: int, row: int, chip_type: str):
    """returns True on win or tie, False on no win"""
    global tie
    consecutive_chips = 0
    for value in board[row]:  # check if there are 4 chip types in a row in variable row
        consecutive_chips = (consecutive_chips + 1) if value == chip_type else 0
        if consecutive_chips == 4:  # the function ends and returns True if it finds 4 in a row
            return True

    consecutive_chips = 0
    for Row in board:  # check if there are 4 rows in a row with chip type in the column number
        consecutive_chips = (consecutive_chips + 1) if Row[col] == chip_type else 0
        if consecutive_chips == 4:  # the function ends and returns True if it finds 4 in a row
            return True

    # check row values in diagonal direction from turn position
    consecutive_chips = 0
    for Row in board:  # first check west to east diagonals
        print(len(board))
        # check rows above current row for diagonal positions

        # then check rows below current row diagonal positions

    # I need to check every row. If '-' does not exist in any row, return a tie game
    for Row in board:
        if '-' not in Row:
            tie = True
        else:
            tie = False
    if tie:
        return True

    return False


current_board = [['-', '-', '-', '-'], ['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]
print_board(current_board)
check_if_winner(current_board)