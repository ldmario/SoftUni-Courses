budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())
video_cards_cost = video_cards * 250
processors_cost = video_cards_cost * 0.35 * processors
ram_cost = video_cards_cost * 0.10 * ram
total_cost = video_cards_cost + processors_cost + ram_cost

if video_cards > processors:
    total_cost *= 0.85

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")