"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class DivisionByZero(Exception):
    def __init__(self, message=None):
        if message is None:
            self.message = "Division by zero"
        else:
            self.message = message


x = int(input("Enter numerator: "))
y = int(input("Enter denominator: "))


def my_func(a, b):
    if b == 0:
        raise DivisionByZero
    else:
        return a / b

try:
    c = my_func(x, y)
except DivisionByZero:
    print("-"*100)
    print("Can not divide by zero")
