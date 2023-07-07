def generating_vector(array, idx):
    if idx == len(vector):
        print(''.join(array))
        return

    for num in range(2):
        array[idx] = str(num)
        generating_vector(array, idx + 1)


len_of_array = int(input())
vector = [None] * len_of_array

generating_vector(vector, 0)
