def loading_bar(percent):
    bar = []
    for _ in range(10):
        bar.append('.')
    current_load = percent // 10
    for index in range(current_load):
        bar[index] = "%"
    x = ''.join(bar)
    return x


integer_input = int(input())
if integer_input == 100:
    print("100% Complete!")
    print(f"[{loading_bar(integer_input)}]")
else:
    print(f"{integer_input}% [{loading_bar(integer_input)}]")
    print("Still loading...")
