list_of_integers = input().split()
number = int(input())
list_of_int = []

for numbers in list_of_integers:
    list_of_int.append(int(numbers))

for _ in range(number):
    list_of_int.remove(min(list_of_int))

print(*list_of_int, sep=", ")
