"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено.
"""
from itertools import cycle

user_list = input("Enter your data divided by comma: ").split(",")

while True:
    try:
        count_of_cycles = int(input("Enter number of cycles (must be integer): "))
        break
    except ValueError:
        print("You enter a string, need integer. Try again.")
        print("-"*100)

my_iterator_2 = cycle(user_list)
count_of_repeating_values = 0

for i in my_iterator_2:
    print(i)
    count_of_repeating_values += 1
    if count_of_repeating_values / len(user_list) == count_of_cycles:
        print("Enclosing cycle")
        print("-" * 100)
        break
    elif (count_of_repeating_values / len(user_list)) in range(1, count_of_cycles):
        print(f"End of {int(count_of_repeating_values / len(user_list))} cycle")
        print("-"*100)
