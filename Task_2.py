"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.
"""

def func_for_naming(name, surname, birth_year, city_of_accomoodation,
                     e_mail, phone_number, **kwargs):
    result = f"Full name of user: {name} {surname}, year of birth: {birth_year}, current location: {city_of_accomoodation}," \
        f" contact phone: {phone_number}, email: {e_mail}."
    if len(kwargs):
        result += " Other features is - "
        i = 0
        for key, value in kwargs.items():
            result += str(key)
            result += ": "
            result += str(value)
            # computing comma or dot in the end of statement.
            i += 1
            if i == len(kwargs):
                result += "."
            else:
                result += ", "
    print(result)





