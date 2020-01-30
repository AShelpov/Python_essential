"""
Программа принимает действительное положительное число x и целое отрицательное число
y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""

def my_power1(root, degree=-1):
    """
    Function accept two positional arguments and exponent argument 'root' in power of argument 'degree'.\n
    Root argument can be integer or float. Considered only positive numbers.\n
    Degree argument can be only integer. Considered only negative numbers\n
    If missing argument 'degree' function considered it as -1.
    :param root: float or integer, only positive
    :param degree: integer, only negative
    :return:
    """
    # checking first argument by type and dimension
    if isinstance(root, (float, int)) == False:
        return "You enter inappropriate type of argument 'root'. Must be float or integer"
    elif float(root) <=0:
        return "You enter inappropriate dimension of argument 'root'. Must be more than zero"
    else:
        root = float(root)

    # checking second argument by type and dimension
    if isinstance(degree, int) == False:
        return "You enter inappropriate type of argument 'degree'. Must be integer"
    elif int(degree) >= 0:
        return "You enter inappropriate dimension of argument 'degree'. Must be less than zero"
    else:
        degree = int(degree)

    return root ** degree




def my_power2(root, degree=-1):
    """
    Function accept two positional arguments and exponent argument 'root' in power of argument 'degree'.\n
    Root argument can be integer or float. Considered only positive numbers.\n
    Degree argument can be only integer. Considered only negative numbers\n
    If missing argument 'degree' function considered it as -1.
    :param root: float or integer, only positive
    :param degree: integer, only negative
    :return:
    """
    # checking first argument by type and dimension
    if isinstance(root, (float, int)) == False:
        return "You enter inappropriate type of argument 'root'. Must be float or integer"
    elif float(root) <=0:
        return "You enter inappropriate dimension of argument 'root'. Must be more than zero"
    else:
        root = float(root)

    # checking second argument by type and dimension
    if isinstance(degree, int) == False:
        return "You enter inappropriate type of argument 'degree'. Must be integer"
    elif int(degree) >= 0:
        return "You enter inappropriate dimension of argument 'degree'. Must be less than zero"
    else:
        degree = int(degree)

    denominator = float(1)
    for i in range(-degree):
        denominator *= root
    return (1 / denominator)


