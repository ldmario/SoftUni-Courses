annual_tax = int(input())
sneakers = annual_tax - (annual_tax * 40 / 100)
basketball_outfit = sneakers - (sneakers * 20 / 100)
basketball_ball = basketball_outfit / 4
basketball_accsesoaries = basketball_ball / 5
total_money_needed = annual_tax + sneakers + basketball_accsesoaries + basketball_outfit + basketball_ball
print(total_money_needed)