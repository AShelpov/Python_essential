"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
"""
from sys import argv

try:
    working_hours = round(float(argv[1]), 2)
    wage_rate_per_hour = round(float(argv[2]), 2)
    premium = round(float(argv[3]), 2)
    if len(argv) == 4:
        print(f"Your salary for the period equals to: {round(working_hours * wage_rate_per_hour + premium, 2)} USD")
        print(f"\tYou have worked for {working_hours} hours.\n"
              f"\tYour salary rate is {wage_rate_per_hour} USD per hour.\n"
              f"\tYour premium for the period is {premium} USD ")
    elif len(argv) == 3:
        print(f"You did not enter premium parameter")
    elif len(argv) == 2:
        print(f"You did not enter premium and wage_rate_per_hour parameters")
    elif len(argv) == 1:
        print(f"You did not enter any parameter")
except ValueError:
    print(f"One of the parameter is not a number")
