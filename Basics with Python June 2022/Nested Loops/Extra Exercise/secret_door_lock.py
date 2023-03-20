first_range = int(input())
second_range = int(input())
third_range = int(input())
number_is_non_prime = False

for i in range(1, first_range + 1):
    for j in range(1, second_range + 1):
        number_is_non_prime = False
        for k in range(1, third_range + 1):
            if i % 2 == 0 and k % 2 == 0 and j == 2:
                print(i, j, k)
            for m in range(2, j):
                if j % m == 0:
                    number_is_non_prime = True
            if i % 2 == 0 and k % 2 == 0:
                if not number_is_non_prime:
                    print(i, j, k)
