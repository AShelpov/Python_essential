"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
порядке их следования в исходном списке. Для выполнения задания обязательно
использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

user_numbers = input("Enter numbers divided by comma: ").split(",")
list_of_numbers = []

for i in user_numbers:
    try:
        list_of_numbers.append(float(i))
    except ValueError:
        print(f"NOTE. One or more of entered symbols is not a number")

output_list = [i for i in list_of_numbers if list_of_numbers.count(i) == 1]
print(output_list)