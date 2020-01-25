"""
Реализовать структуру « Рейтинг », представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.
"""
while True:
    user_list_of_ratings = input("Enter list of initial ratings (must be integers), divided by gap : ").split(" ")
    try:
        initial_list_of_ratings = []
        for i in user_list_of_ratings:
            initial_list_of_ratings.append(int(i))
        initial_list_of_ratings.sort(reverse=True)
    except ValueError:
        print()
        print("You enter a string or a float or something else.\nTry again please.")
        print("="*100)
        continue
    else:
        break

print("="*100)
print("Now you will add additional rating numbers, it must be only string and only one per iteration.\n"
      "If you want to stop adding new items type 'Stop', this will end program and return final list of ratings.")

final_list_of_ratings = initial_list_of_ratings
while True:
    user_command = input("Please enter new rating. It must be integer and one per time: ")
    print("-"*100)
    if user_command.lower() == "stop":
        print("Your final list of ratings is: ", *final_list_of_ratings)
        print("Program have been ended")
        print("*"*100)
        break
    try:
        user_command = int(user_command)
        final_list_of_ratings.append(user_command)
        final_list_of_ratings.sort(reverse=True)
        print("Your current list of ratings is: ", *final_list_of_ratings)
        print("="*100)
    except ValueError:
        print()
        print("You enter a string or a float or something else, but not an integer.\nTry again please.\n"
              "You can enter only one integer per time or 'Stop' command to over the program")
        print("Your current list of ratings is: ", *final_list_of_ratings)
        print("=" * 100)
        continue






