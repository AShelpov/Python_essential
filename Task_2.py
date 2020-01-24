"""Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать
функцию input() ."""

while True:
    my_list = input("Enter minimum two strings or numbers divided by gap: ").split(" ")
    if len(my_list) == 1 and my_list[0] == "":
        print("=" * 100)
        print("You didn't enter anything.\nPlease try again!")
        print("="*100)
        continue
    elif len(my_list) == 1:
        print("=" * 100)
        print("You didn't divide your data by gap or enter one sequence.\nNeed two or more.\nPlease try again!")
        print("="*100)
    else:
        break

if len(my_list) % 2 == 0:
    inverse_list = []
    i = 0
    while (i / 2) != len(my_list) / 2:
        temp_list = [my_list[i + 1], my_list[i]]
        inverse_list.append(temp_list)
        i += 2
    print(sum(inverse_list, []))
else:
    inverse_list = []
    i = 0
    while (i / 2) != (len(my_list) - 1) / 2:
        temp_list = [my_list[i + 1], my_list[i]]
        inverse_list.append(temp_list)
        i += 2
    inverse_list = sum(inverse_list, [])
    inverse_list.append(my_list[-1])
    print(inverse_list)


