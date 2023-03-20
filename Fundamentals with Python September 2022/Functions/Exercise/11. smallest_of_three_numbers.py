def smallest_number(a, b, c):
    return min(a, b, c)


first_num = int(input())
second_num = int(input())
third_num = int(input())

smallest = smallest_number(first_num, second_num, third_num)

print(smallest)
