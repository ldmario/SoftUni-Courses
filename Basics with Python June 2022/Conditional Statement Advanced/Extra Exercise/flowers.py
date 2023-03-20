chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
bouquet = 0
flowers = chrysanthemums + roses + tulips
if season == "Spring" or season == "Summer":
    if holiday == "N":
        bouquet = chrysanthemums * 2 + roses * 4.10 + tulips * 2.50
        if tulips > 7 and season == "Spring":
            bouquet *= 0.95
        if flowers > 20:
            bouquet *= 0.80
    elif holiday == "Y":
        bouquet = (chrysanthemums * 2 + roses * 4.10 + tulips * 2.50) * 1.15
        if tulips > 7 and season == "Spring":
            bouquet *= 0.95
        if flowers > 20:
            bouquet *= 0.80
if season == "Autumn" or season == "Winter":
    if holiday == "N":
        bouquet = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
        if roses >= 10 and season == "Winter":
            bouquet *= 0.90
        if flowers > 20:
            bouquet *= 0.80
    elif holiday == "Y":
        bouquet = (chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15) * 1.15
        if roses >= 10 and season == "Winter":
            bouquet *= 0.90
        if flowers > 20:
            bouquet *= 0.80

print(f"{bouquet + 2:.2f}")
