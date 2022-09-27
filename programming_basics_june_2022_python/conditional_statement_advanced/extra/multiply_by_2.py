number = 0
while number >= 0:
    number = float(input())
    if number < 0:
        print("Negative number!")
        break
    number *= 2
    print(f"Result: {number:.2f}")
    continue
