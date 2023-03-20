product = input()
quantity = int(input())

coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00


def total_price(product_type, amount_of_product):
    if product_type == "water":
        return amount_of_product * water
    elif product_type == "coffee":
        return amount_of_product * coffee
    elif product_type == "coke":
        return amount_of_product * coke
    elif product_type == "snacks":
        return amount_of_product * snacks


final_price = total_price(product, quantity)

print(f"{final_price:.2f}")
