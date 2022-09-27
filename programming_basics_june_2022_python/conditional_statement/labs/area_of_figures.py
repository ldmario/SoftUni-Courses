from math import pi

type_of_figure = input()
if type_of_figure == "square":
    length_of_his_side: float = float(input())
    area_of_square = length_of_his_side * length_of_his_side
    print(f"{area_of_square:.3f}")
elif type_of_figure == "rectangle":
    length_of_first_side = float(input())
    length_of_second_side = float(input())
    area_of_rectangle = length_of_first_side * length_of_second_side
    print(f"{area_of_rectangle:.3f}")
elif type_of_figure == "circle":
    radius = float(input())
    area_of_circle = pi * radius**2
    print(f"{area_of_circle:.3f}")
elif type_of_figure == "triangle":
    length_of_side = float(input())
    height_of_triangle = float(input())
    area_of_triangle = length_of_side * height_of_triangle / 2
    print(f"{area_of_triangle:.3f}")
