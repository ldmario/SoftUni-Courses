x = float(input())
y = float(input())
h = float(input())
infront_and_back_wall = (x * x - 1.2 * 2) + (x * x)
side_walls = (2 * y * x) - (2 * 1.5 * 1.5)
top_of_the_roof = 2 * x * y
side_of_the_roof = 2 * x * h / 2
green_paint = (side_walls + infront_and_back_wall) / 3.4
red_paint = (top_of_the_roof + side_of_the_roof) / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")