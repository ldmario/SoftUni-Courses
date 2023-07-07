def read_lab():
    lab = []
    for _ in range(r):
        lab.append(list(input()))
    return lab


def is_exit(row, col, matrix):
    if matrix[row][col] == 'e':
        return True
    return False


def is_free(row, col, matrix):
    if matrix[row][col] != 'v':
        return True
    return False


def valid_borders(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return True
    return False


def is_wall(row, col, matrix, path):
    if matrix[row][col] == '*':
        path.pop()
        return True
    return False


def print_path(path):
    print(''.join(path))


def mark_visited(row, col, matrix, type):
    matrix[row][col] = type


def find_path(row, col, direction, matrix, path):
    if valid_borders(row, col, matrix):
        return

    path.append(direction)

    if is_exit(row, col, matrix):
        print_path(path)

    elif is_wall(row, col, matrix, path):
        return

    elif is_free(row, col, matrix):

        mark_visited(row, col, matrix, 'v')
        find_path(row, col + 1, 'R', matrix, path)
        find_path(row, col - 1, 'L', matrix, path)
        find_path(row + 1, col, 'D', matrix, path)
        find_path(row - 1, col, 'U', matrix, path)
        mark_visited(row, col, matrix, '-')

    path.pop()


r = int(input())
c = int(input())
labyrinth = read_lab()
find_path(0, 0, '', labyrinth, [])
