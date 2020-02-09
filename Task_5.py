"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os as os

with open("Text_file_for_task5.txt", "w") as numeral_file:
    list_of_numbers = [input("Enter numbers, divided by comma. Must be float or integers: ") \
                       for j in range(int(input("Enter number of strings, must be integers: ")))]
    for i in list_of_numbers:
        numeral_file.write(str(i) + "\n")


output_sum = 0
with open("Text_file_for_task5.txt", "r") as reading_file:
    for line in reading_file:
        numbers_list = line.split(",")
        for i in numbers_list:
            try:
                output_sum += float(i)
            except ValueError:
                continue
print(output_sum)

os.remove(os.path.join(os.getcwd(), "Text_file_for_task5.txt"))