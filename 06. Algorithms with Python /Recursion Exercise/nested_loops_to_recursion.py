def nested_loops(array, idx):
    if idx == len(array):
        print(' '.join(array))
        return

    for num in range(1, len(array) + 1):
        array[idx] = str(num)
        nested_loops(array, idx + 1)


n = int(input())
array = [None] * n
nested_loops(array, 0)
