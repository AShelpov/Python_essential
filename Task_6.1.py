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
from itertools import count

while True:
    try:
        start_number = int(input("Enter start number (must be integer): "))
        break
    except ValueError:
        print("You enter a string, need integer. Try again.")
        print("-"*100)

while True:
    try:
        stop_number = int(input("Enter stop number (must be integer): "))
        break
    except ValueError:
        print("You enter a string, need integer. Try again.")
        print("-" * 100)

my_iterator_1 = count(start=start_number)
for i in my_iterator_1:
    print(i)
    if i == stop_number:
        break
