junior_bikers = int(input())
senior_bikers = int(input())
type_terrain = input()
collected_money = 0
if type_terrain == "trail":
    collected_money = junior_bikers * 5.50 + senior_bikers * 7
elif type_terrain == "cross-country":
    total_participants = senior_bikers + junior_bikers
    collected_money = junior_bikers * 8 + senior_bikers * 9.50
    if total_participants >= 50:
        collected_money *= 0.75
elif type_terrain == "downhill":
    collected_money = junior_bikers * 12.25 + senior_bikers * 13.75
elif type_terrain == "road":
    collected_money = junior_bikers * 20 + senior_bikers * 21.50

collected_money *= 0.95

print(f"{collected_money:.2f}")