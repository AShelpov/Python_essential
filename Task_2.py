"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

import os as os
# write text file
my_string = "The path of the righteous man is beset on all sides by the inequities of the selfish \n" \
            "and the tyranny of evil men. Blessed is he who, in the name of charity and good will, \n" \
            "shepherds the weak through the valley of darkness, \n" \
            "for he is truly his brother's keeper and the finder of lost children.\n" \
            "And I will strike down upon thee with great vengeance and furious anger those \n" \
            "who attempt to poison and destroy my brothers.\n" \
            "And you will know my name is the Lord when I lay my vengeance upon thee."

with open("Text_file_for_task2.txt", "w") as input_file:
    input_file.write(my_string)



with open("Text_file_for_task2.txt", "r") as my_file:
    counter_of_symbols = []
    for line in my_file:
        counter_of_symbols.append(len(line))

os.remove(os.path.join(os.getcwd(), "Text_file_for_task2.txt"))

for i in enumerate(counter_of_symbols):
    print(f"Line number {i[0] + 1} with {i[1]} characters")