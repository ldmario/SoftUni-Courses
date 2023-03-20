price_of_skumriq = float(input())
price_of_caca = float(input())
kilogram_of_palamud = float(input())
kilogram_of_safrid = float(input())
kilogram_of_mussels = int(input())
price_of_palamud = kilogram_of_palamud * (price_of_skumriq + price_of_skumriq * 0.60)
price_of_safrid = kilogram_of_safrid * (price_of_caca + price_of_caca * 0.80)
price_of_mussels = kilogram_of_mussels * 7.50
total_price = price_of_mussels + price_of_palamud + price_of_safrid
print(f"{total_price:.2f}")
