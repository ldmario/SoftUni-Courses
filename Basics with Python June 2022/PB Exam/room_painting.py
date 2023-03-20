from math import ceil, floor

boxes_paint = int(input())
rolls_wallpaper = int(input())
price_pair_gloves = float(input())
price_for_brush = float(input())

price_paint = boxes_paint * 21.5
price_wallpapers = rolls_wallpaper * 5.20
needed_gloves = ceil(rolls_wallpaper * 0.35)
needed_brushes = floor(boxes_paint * 0.48)
total_price_gloves = price_pair_gloves * needed_gloves
total_price_brushes = price_for_brush * needed_brushes

total_price = total_price_gloves + total_price_brushes + price_paint + price_wallpapers

price_delivery = total_price / 15

print(f"This delivery will cost {price_delivery:.2f} lv.")
