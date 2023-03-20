period = int(input())

doctors = 7
treated_patients = 0
non_treated_patients = 0

for day in range(1, period + 1):
    if day % 3 == 0 and non_treated_patients > treated_patients:
        doctors += 1
    amount_patients = int(input())
    if doctors >= amount_patients:
        treated_patients += amount_patients
    else:
        treated_patients += doctors
        non_treated_patients += amount_patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {non_treated_patients}.")
