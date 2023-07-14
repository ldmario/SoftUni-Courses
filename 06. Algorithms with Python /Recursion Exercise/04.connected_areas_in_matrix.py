class Area:
    def __init__(self, row, col, size):
        self.size = size
        self.col = col
        self.row = row


def is_border(row, col, rows, cols):
    if row > rows - 1 or col > cols - 1 or row < 0 or col < 0:
        return True
    return False


def is_valid(row, col, matrix):
    if matrix[row][col] != '-':
        return True
    return False


def find_areas(row, col, rows, cols, matrix):
    if is_border(row, col, rows, cols):
        return 0

    if is_valid(row, col, matrix):
        return 0

    matrix[row][col] = 'v'
    result = 1
    result += find_areas(row, col + 1, rows, cols, matrix)
    result += find_areas(row, col - 1, rows, cols, matrix)
    result += find_areas(row + 1, col, rows, cols, matrix)
    result += find_areas(row - 1, col, rows, cols, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = [[x for x in input()] for _ in range(rows)]

areas = []
for row in range(rows):
    for col in range(cols):
        size = find_areas(row, col, rows, cols, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f"Total areas found: {len(areas)}")
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f"Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}")
