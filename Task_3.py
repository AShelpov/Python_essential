"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""

def my_func(a=0, b=0, c=0, *args):
    """
    Function expect three argument and return the sum of the two greatest of them.
    If would be passed less then three arguments, function will estimate missing as null.
    Function can accept more than three arguments, but returns sum of the two greatest considered additional values
    Function expect arguments as integer or float. But it won't raise error if transfer other types.
    It will consider such argument as null
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :param args: int or float
    :return: int or float
    """
    expected_values = [a if isinstance(a, (int, float)) else 0,
                       b if isinstance(b, (int, float)) else 0,
                       c if isinstance(c, (int, float)) else 0]
    unexpected_values = [i for i in args if isinstance(i, (int, float))]
    computing_list = expected_values + unexpected_values
    computing_list = sorted(computing_list, reverse=True)

    return computing_list[0] + computing_list[1]

