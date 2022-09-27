start_range = int(input())
end_range = int(input())

for symbol in range(start_range, end_range + 1):
    letter = chr(symbol)
    print(letter, end=" ")
