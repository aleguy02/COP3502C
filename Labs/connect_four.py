def initialize_board(num_rows: int, num_cols: int):  # Creates a blank board based on how tall and long the user wants
    board = []
    for i in range(num_rows):
        board.append([])
        for j in range(num_cols):
            board[i].append('-')
    return board


def print_board(board: list):
    for row in board:
        for col_val in row:
            print(col_val, end=' ')
        print()


def insert_chip(board: list, col, chip_type):
    pass


height = int(input('What would you like the height of the board to be? '))
length = int(input('What would you like the length of the board to be? '))
print_board((initialize_board(height, length)))
