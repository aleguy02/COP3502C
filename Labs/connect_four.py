def initialize_board(num_rows: int, num_cols: int):  # Creates a blank board based on how tall and long the user wants
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


def insert_chip(board: list, col, chip_type):
    x = 0
    for row in board:
        if row[col] == '-':  # insert chip_type into board[rowvalue][col]
            row.pop(col)
            row.insert(col, chip_type)
            break
        x += 1

    return x


def check_if_winner(board: list, col: int, row: int, chip_type: str):
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

    return False


# start of the game here
