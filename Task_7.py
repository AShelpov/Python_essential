"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
Подсказка: использовать менеджер контекста.
"""
import random as rnd
import json as json
import os as os

list_of_names = ["Horns", "Hooves", "Chamomile", "Titmouse", "Iris", "Car", "Welo", "Halo", "Common", "ResPublica"]
type_of_ownership = ["Ltd.", "Inc.", "GmbH", "LLC", "AG"]

with open("Text_file_for_task7.txt", "w") as input_file:
    repeating_names = []
    for i in range(len(list_of_names)):
        while True:
            name = rnd.choice(list_of_names)
            ownership = rnd.choice(type_of_ownership)
            if name in repeating_names:
                continue
            else:
                input_file.write(f"{name} {ownership} {round(rnd.uniform(50000, 100000), 2)}"
                                 f" {round(rnd.uniform(40000, 90000), 2)}\n")
                repeating_names.append(name)
                break

with open("Text_file_for_task7.txt", "r") as reading_file:
    for_average_profit = []
    output_list = []
    for line in reading_file:
        name = line.split()[0]
        revenue = float(line.split()[2])
        expenses = float(line.split()[3])
        profit = round(revenue - expenses, 2)

        if profit > 0:
            for_average_profit.append(profit)
        output_list.append({name: profit})

    output_list.append({"average_profit": round(sum(for_average_profit) / len(for_average_profit), 2)})

os.remove(os.path.join(os.getcwd(), 'Text_file_for_task7.txt'))

with open("Output_file_of_task7.json", "w") as writing_file:
    json.dump(output_list, writing_file)
