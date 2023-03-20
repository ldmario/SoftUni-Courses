def add_and_subtract(x: int, y: int, z: int):
    def sum_numbers():
        return x + y

    def subtract():
        return sum_numbers() - z

    return subtract()


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
