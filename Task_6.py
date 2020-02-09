"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import os as os

lessons = ["Math", "English", "Russian", "Physics", "Biology", "Chemistry"]
lectures = [100, "-", 90, 80, 50, 90]
seminars = [200, 50, "-", 200, 150, 200]
laboratories = ["-", "-", "-", 150, 50, 100]

with open("Text_file_for_task6.txt", "w") as input_file:
    for i in zip(lessons, lectures, seminars, laboratories):
        string_of_lesson = i[0] + " " + str(i[1]) + "(lectures) " + str(i[2]) + "(seminars) " + str(i[3]) \
                           + "(laboratories)" + "\n"
        input_file.write(string_of_lesson)

output_dict = {}

with open("Text_file_for_task6.txt", "r") as reading_file:
    for line in reading_file:
        lesson = line.split()[0]
        lectures = line.split()[1]
        seminars = line.split()[2]
        laboratories = line.split()[3]
        try:
            lectures = int(lectures[:lectures.find("(")])
        except ValueError:
            lectures = 0

        try:
            seminars = int(seminars[:seminars.find("(")])
        except ValueError:
            seminars = 0

        try:
            laboratories = int(laboratories[:laboratories.find("(")])
        except ValueError:
            laboratories = 0

        output_dict[lesson] = lectures + seminars + laboratories

os.remove(os.path.join(os.getcwd(), "Text_file_for_task6.txt"))

print(output_dict)