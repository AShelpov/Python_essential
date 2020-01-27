"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
list_of_month = ["winter", "winter", "spring", "spring", "spring", "summer",
                 "summer", "summer", "autumn", "autumn", "autumn", "winter"]
dict_of_month = {12: "winter", 1: "winter", 2: "winter",
                 3: "spring", 4: "spring", 5: "spring",
                 6: "summer", 7: "summer", 8: "summer",
                 9: "autumn", 10: "autumn", 11: "autumn"}
while True:
    user_month = input("Enter serial number of month: ")
    try:
        user_month = int(user_month)
        if user_month in range(1, 13):
            break
        else:
            print()
            print("You enter wrong number. Must be in range from 1 to 12.\nTry again")
            print("=" * 100)
            continue
    except ValueError:
        try:
            float(user_month)
        except ValueError:
            print()
            print("You enter string, need integer from 1 to 12.\nTry again")
            print("=" * 100)
            continue
        else:
            print()
            print("You enter float number, need integer from 1 to 12.\nTry again")
            print("=" * 100)
            continue
    except Exception:
        print()
        print("Hmmm....Strange thing had happened.\nTry again")
        print("=" * 100)
        continue

print()
print("*"*50, "solution by using list", "*"*50)
print(f"Your month has come in the {list_of_month[user_month - 1]}")
print()
print("*"*50, "solution by using dictionary", "*"*50)
print(f"Your month has come in the {dict_of_month[user_month]}")