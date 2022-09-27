package_kilograms = float(input())
service_type = input()
distance = int(input())
total_price = 0
increase_for_kg = 0
total_price_after_increase = 0
if service_type == "standard":
    if package_kilograms < 1:
        total_price = distance * 0.03
    elif 1 <= package_kilograms < 10:
        total_price = distance * 0.05
    elif 10 <= package_kilograms < 40:
        total_price = distance * 0.10
    elif 40 <= package_kilograms < 90:
        total_price = distance * 0.15
    elif 90 <= package_kilograms < 150:
        total_price = distance * 0.20
elif service_type == "express":
    if package_kilograms < 1:
        total_price = distance * 0.03
        increase_for_kg = 0.03 * 0.80
    elif 1 <= package_kilograms < 10:
        total_price = distance * 0.05
        increase_for_kg = 0.05 * 0.40
    elif 10 <= package_kilograms < 40:
        total_price = distance * 0.10
        increase_for_kg = 0.10 * 0.05
    elif 40 <= package_kilograms < 90:
        total_price = distance * 0.15
        increase_for_kg = 0.15 * 0.02
    elif 90 <= package_kilograms < 150:
        total_price = distance * 0.20
        increase_for_kg = 0.20 * 0.01

    increase_for_km = package_kilograms * increase_for_kg
    total_increase = distance * increase_for_km
    total_price_after_increase = total_price + total_increase

if service_type == "standard":
    print(f"The delivery of your shipment with weight of {package_kilograms:.3f} kg. would cost {total_price:.2f} lv.")
elif service_type == "express":
    print(f"The delivery of your shipment with weight of {package_kilograms:.3f} "
          f"kg. would cost {total_price_after_increase:.2f} lv.")
