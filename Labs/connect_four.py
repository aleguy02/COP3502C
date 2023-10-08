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
    for row in board:
        if row[col] == '-':  # insert chip_type into board[rowvalue][col]
            row.pop(col)
            row.insert(col, chip_type)
            break

    return board

    # replace column value with chip_type if the column value is open (-) in the first row
    # if the column value is not open in the first row, check the next row
    # store the row number


# start of the game here
height = 4
length = 4

current_board = initialize_board(height, length)
print_board(current_board)
print()

turn_col = 2
current_board = insert_chip(current_board, turn_col, 'x')
print_board(current_board)
print()

turn_col = 2
current_board = insert_chip(current_board, turn_col, 'x')
print_board(current_board)