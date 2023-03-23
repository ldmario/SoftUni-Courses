destination = input()
budget = 0
while destination != "End":
    budget = 0
    min_budget = float(input())
    while budget < min_budget:
        current_sum = float(input())
        budget += current_sum
        if budget >= min_budget:
            print(f"Going to {destination}!")
    destination = input()
