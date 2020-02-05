"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция должна
вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала
числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce

while True:
    try:
        n = int(input("Enter number, must be integer: "))
        break
    except ValueError:
        print("You enter a string or something else. Try again")
        print("-"*100)



def fuctorial(n=0):
    output = 1
    for i in range(1, n+1):
        output *= i
        yield output


for el in fuctorial(n):
    output = str(el)
    if len(output) >= 15:
        print(output[:15])
    else:
        print(output)



