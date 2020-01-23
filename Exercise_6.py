a = float(input("Kilometers is first day: "))
b = float(input("Target by kilometers: "))
nex_day_result = a
counter_of_days = 1
while nex_day_result < b:
    nex_day_result *= 1.1
    counter_of_days += 1

print(f"Sportsmen will catch his goal within {counter_of_days} days")