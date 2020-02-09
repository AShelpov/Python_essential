"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

# make text file with random choice
import random as rnd
import os as os

list_of_employees = ["Nadine Merrell", "Maya Lesniak", "Mae Griego", "Dennis Ratzlaff", "Harriett Bastian",
                     "Vanesa Piersall", "Shantell Guild", "Elissa You", "Jerrie Vitale", "Emory Hursh", "Breann Bryson",
                     "Charolette Trace", "Martine Penick", "Nadene Kaba", "Rosalba Sautner", "Carl Lightner"]

with open("Text_file_for_task3.txt", "w") as salary_book:
    repeating_names = []
    for i in range(len(list_of_employees)):
        while True:
            name = rnd.choice(list_of_employees)
            if name in repeating_names:
                continue
            else:
                salary_book.write(name + ": " + str(round(rnd.uniform(10000,30000), 2)) + "\n")
                repeating_names.append(name)
                break


with open("Text_file_for_task3.txt", "r") as input_file:
    for_average_salary = []
    list_of_little_earnings_employees = []
    for line in input_file:
        employee = line.split(":")
        for_average_salary.append(float(employee[1]))

        if float(employee[1]) < 20000:
            list_of_little_earnings_employees.append(line)

os.remove(os.path.join(os.getcwd(), "Text_file_for_task3.txt"))

print("List of employees with earnings less than 20 000")
for i in list_of_little_earnings_employees:
    print(i, end="")
print("-"*100)
print(f"Average salary for all employees is equal to {round(sum(for_average_salary) / len(for_average_salary), 2)} USD")