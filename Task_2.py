"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения
которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
user_numbers = input("Enter numbers divided by comma: ").split(",")
list_of_numbers = []

for i in user_numbers:
    try:
        list_of_numbers.append(float(i))
    except ValueError:
        print(f"NOTE. one or more of entered symbols is not a number")

output_list = [list_of_numbers[i + 1] for i in range(len(list_of_numbers) - 1)\
               if list_of_numbers[i + 1] > list_of_numbers[i]]

print(list_of_numbers)
print(output_list)