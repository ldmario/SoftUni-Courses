quantity_tabs = int(input())
salary = int(input())

for tabs in range(1, quantity_tabs + 1):
    if salary <= 0:
        break
    else:
        type_of_tab = input()
        if type_of_tab == "Facebook":
            salary -= 150
        elif type_of_tab == "Instagram":
            salary -= 100
        elif type_of_tab == "Reddit":
            salary -= 50

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
