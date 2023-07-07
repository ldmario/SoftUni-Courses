rows = int(input())


def drawing(row):
    if row <= 0:
        return

    print('*' * row)
    drawing(row - 1)
    print('#' * row)


drawing(rows)
