price_for_kilogram_vegetables = float(input())
price_for_kilogram_fruits = float(input())
total_vegetables_kilograms = int(input())
total_fruits_kilograms = int(input())
price_vegetables_in_euro = price_for_kilogram_vegetables / 1.94
price_fruits_in_euro = price_for_kilogram_fruits / 1.94
total_price = total_fruits_kilograms * price_fruits_in_euro + total_vegetables_kilograms * price_vegetables_in_euro
print(f"{total_price:.2f}")
