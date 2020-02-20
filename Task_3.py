"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
"""


class IsNotNumber(Exception):
    def __init__(self, message=None):
        if message is None:
            self.message = "Is not number"
        else:
            self.message = message


def is_number(element):
    try:
        element = float(element)
        return element
    except ValueError:
        raise IsNotNumber


list_of_numbers = []
while True:
    new_element = input("Enter new element, must be number: ")
    if "stop" in new_element.lower():
        print(list_of_numbers)
        break
    else:
        try:
            list_of_numbers.append(is_number(new_element))
        except IsNotNumber:
            print("You input not a number")
            print("-"*100)
            continue



