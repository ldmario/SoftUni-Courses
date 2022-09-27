paper = int(input())
cloth = int(input())
glue = float(input())
discount = int(input())

price_paper = paper * 5.80
price_cloth = cloth * 7.20
price_glue = glue * 1.20
total_price = price_glue + price_cloth + price_paper
total_price_discount = total_price * discount / 100
total_after_price_discount = total_price - total_price_discount

print(f"{total_after_price_discount:.3f}")
