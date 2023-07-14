def move_down_right(row, col, rows, cols, board, moves):
    if row == rows - 1 and col == cols - 1:
        moves.append(1)
        return
    if col > len(board[0]) - 1:
        return
    if row > len(board) - 1:
        return

    board[row][col] = 'v'
    move_down_right(row, col + 1,rows, cols, board, moves)
    move_down_right(row + 1, col,rows, cols, board, moves)
    board[row][col] = '-'

    return len(moves)


rows = int(input())
cols = int(input())

moves_counter = []

matrix = [['-'] * cols for row in range(rows)]

print(move_down_right(0, 0, rows, cols, matrix, moves_counter))
