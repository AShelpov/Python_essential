"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
только первые 10 букв в слове.
"""

while True:
    my_list = input("Enter string with minimum two words divided by gap: ").split(" ")
    if len(my_list) == 1 and my_list[0] == "":
        print()
        print("You didn't enter anything.\nPlease try again!")
        print("="*100)
        continue
    elif len(my_list) == 1:
        print()
        print("You didn't divide your string by gap or enter one word.\nNeed two or more.\nPlease try again!")
        print("="*100)
    else:
        break

for i, word in enumerate(my_list):
    print(i + 1, word if len(word) < 10 else word[:10])

