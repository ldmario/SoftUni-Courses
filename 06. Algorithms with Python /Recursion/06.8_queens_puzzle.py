def end_of_board(row, board):
    if row >= len(board):
        return True
    return False


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def add_squares_taken(row, board, col, rows, cols, left_diags, right_diags):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diags.add(col - row)
    right_diags.add(col + row)


def remove_squares_taken(row, board, col, rows, cols, left_diags, right_diags):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diags.remove(col - row)
    right_diags.remove(col + row)


def valid_square(row, col, rows, cols, left_diags, right_diags):
    if row in rows:
        return False
    if col in cols:
        return False
    if col - row in left_diags:
        return False
    if col + row in right_diags:
        return False

    return True


def put_queen(row, board, rows, cols, left_diags, right_diags):
    if end_of_board(row, board):
        print_board(board)
        return

    for col in range(8):
        if valid_square(row, col, rows, cols, left_diags, right_diags):
            add_squares_taken(row, board, col, rows, cols, left_diags, right_diags)
            put_queen(row + 1, board, rows, cols, left_diags, right_diags)
            remove_squares_taken(row, board, col, rows, cols, left_diags, right_diags)


taken_rows = set()
taken_cols = set()
taken_left_diag = set()
taken_right_diag = set()

n = 8
board = [['-'] * n for _ in range(8)]

put_queen(0, board, taken_rows, taken_cols, taken_left_diag, taken_right_diag)
