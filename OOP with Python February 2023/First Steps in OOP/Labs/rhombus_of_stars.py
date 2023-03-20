def up_part(n):
    for row_up in range(1, n + 1):
        if row_up < n:
            print(" " * (n - row_up), end="")
        for col in range(row_up):
            print("*", end=" ")
        print()


def down_part(n):
    for row_down in range(n - 1, 0, -1):
        if row_down < n:
            print(" " * (n - row_down), end="")
        for col in range(row_down):
            print("*", end=" ")
        print()


n = int(input())
up_part(n), down_part(n)