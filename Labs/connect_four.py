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


def insert_chip(board: list, col: int, chip_type):
    board_row = 0
    for row in board:
        if row[col] == '-':  # insert chip_type into board[rowvalue][col]
            row.pop(col)
            row.insert(col, chip_type)
            break
        board_row += 1

    return board_row


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

    # add diagonal check here
    consecutive_chips = 0
    for i in range(-3, 4):  # checks up and to the right starting from 3 positions down and to the left of the turn position
        if 0 <= row + i < len(board) and 0 <= col + i < len(board[row]):  # these criteria ensure that we stay in the bounds of the board size
            if board[row + i][col + i] == chip_type:
                consecutive_chips += 1
            else:
                consecutive_chips = 0
        if consecutive_chips == 4:
            return True

    consecutive_chips = 0
    for i in range (-3, 4):  # checks up and to the left starting from 3 positions down and to the right of the turn position
        if 0 <= row + i < len(board) and 0 <= col - i < len(board[row]):
            if board[row + i][col - i] == chip_type:
                consecutive_chips += 1
            else:
                consecutive_chips = 0
        if consecutive_chips == 4:
            return True



    # I need to check every row. If '-' does not exist in any row, return a tie game
    for Row in board:
        if '-' not in Row:
            tie = True
        else:
            tie = False
    if tie:
        return True

    return False


if __name__ == '__main__':
    height = int(input('What would you like the height of the board to be? '))
    length = int(input('What would you like the length of the board to be? '))

    current_board = initialize_board(height, length)  # makes board the size the user wants
    print_board(current_board)

    print('Player 1: x\nPlayer 2: o')

    # game starts here
    x = 1
    while True:
        if x % 2 == 0:  # need to alternate between player
            player_num = 2
            player_chip = 'o'
        else:
            player_num = 1
            player_chip = 'x'
        x += 1

        turn_col = int(input(f'Player {player_num}: Which column would you like to choose? '))
        turn_row = insert_chip(current_board, turn_col, player_chip)
        print_board(current_board)

        tie = False
        if check_if_winner(current_board, turn_col, turn_row, player_chip):
            if tie:
                print('Draw. Nobody wins.')
            else:
                print(f'Player {player_num} won the game!')
            break
