"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open("output_file_task1.txt", mode="w") as output_file:
    while True:
        user_input = input("Enter some string here: ")
        if user_input == "":
            break
        else:
            user_input += "\n"
            output_file.write(user_input)