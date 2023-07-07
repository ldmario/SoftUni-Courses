def calc_sum(idx, numbers):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + calc_sum(idx + 1, numbers)


array = list(map(int, input().split(' ')))

print(calc_sum(0, array))
