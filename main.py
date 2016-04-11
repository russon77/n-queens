
board_width = board_height = 8


def is_valid_position(row, col, queens):
    # check if row or column is occupied
    if any(map(lambda x: x['row'] == row or x['col'] == col, queens)):
        return False

    # check diagonals
    if any(map(lambda x: abs(x['row'] - row) == abs(x['col'] - col), queens)):
        return False

    return True


def possible_moves(current_queens):
    for row in range(0, board_height):
        for col in range(0, board_width):
            move = {'row': row, 'col': col}
            if move not in current_queens:
                yield move


def n_queens(num_queens, current_queens):
    if 0 == num_queens:
        return current_queens

    for move in possible_moves(current_queens):
        if is_valid_position(move['row'], move['col'], current_queens):
            tmp = n_queens(num_queens - 1, [move] + current_queens)
            if tmp is not None:
                return tmp


def display_board(queens):
    if queens is None:
        return

    board = []
    for row in range(0, board_height):
        board.append(['Q' if {'row': row, 'col': col} in queens else ' ' for col in range(0, board_width)])

    return board


if __name__ == '__main__':
    for i in range(0, 9):
        [print(row) for row in display_board(n_queens(i, []))]
        print() # new line
