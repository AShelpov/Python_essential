"""
Реализовать структуру « Рейтинг », представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.
"""

final_list_of_ratings = []
while True:
    user_command = input("Please enter new rating. It must be integer and one per time.\n"
                         "If you want stop program enter 'Stop': ")
    print("-"*100)
    if user_command.lower() == "stop":
        print("Your final list of ratings is: ", *final_list_of_ratings)
        print("Program have been ended")
        print("*"*100)
        break
    # accept only integers and only one per iteration
    try:
        user_number = abs(int(user_command))
        # if list of ratings is empty
        if len(final_list_of_ratings) == 0:
            final_list_of_ratings.append(user_number)
        # if only one record in list of rating
        elif len(final_list_of_ratings) == 1:
            if final_list_of_ratings[0] > user_number:
                final_list_of_ratings.append(user_number)
            else:
                final_list_of_ratings.insert(0, user_number)
        # for two and more records in list of rating
        else:
            # if rating has such value in list of ratings
            if user_number in final_list_of_ratings:
                new_index = final_list_of_ratings.index(user_number) + final_list_of_ratings.count(user_number)
                final_list_of_ratings.insert(new_index, user_number)
            # if value of rating new in list of ratings
            else:
                # for circumstances when new number is greater than all in list of ratings
                if final_list_of_ratings[0] < user_number:
                    final_list_of_ratings.insert(0, user_number)
                # for circumstances when new number is less than all in list of ratings
                elif final_list_of_ratings[-1] > user_number:
                    final_list_of_ratings.append(user_number)
                # for circumstances when new number between numbers in space of list of integers
                else:
                    for i in range(len(final_list_of_ratings)):
                        if final_list_of_ratings[i] > user_number > final_list_of_ratings[i + 1]:
                            new_index = i + 1 + final_list_of_ratings.count(user_number)
                            final_list_of_ratings.insert(new_index, user_number)
                            break
    except ValueError:
        print()
        print("You enter a string or a float or something else, but not an integer.\nTry again please.\n"
              "You can enter only one integer per time or 'Stop' command to over the program")
        print("Your current list of ratings is: ", *final_list_of_ratings)
        print("=" * 100)
        continue






