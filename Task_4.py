"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""
import os as os

my_string = "One - 1\n" \
            "Two - 2\n" \
            "Three - 3\n" \
            "Four - 4\n"

with open("Text_file_for_task4.txt", "w") as my_file:
    my_file.write(my_string)


numeral_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("Output_text_file_of_task4.txt", "w", encoding="utf-8") as output_file:
    with open("Text_file_for_task4.txt", "r") as reading_file:
        for line in reading_file:
            if line.split()[0] in numeral_dict.keys():
                new_text = line.replace(line.split()[0], numeral_dict[line.split()[0]])
                output_file.write(new_text)

os.remove(os.path.join(os.getcwd(), "Text_file_for_task4.txt"))