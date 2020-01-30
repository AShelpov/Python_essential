"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.
"""


def sum_of_numbers(previous_sum=0):
    """
    Recursion function. Accept only integers and floats. Command "Stop" will over computing and return
    sum of numbers. Argument "previous_sum" is default by zero and mostly using in inner function algorithm.
    But if you want start summing from a number other than zero, input this number in function
    If function determine inappropriate input, it will return previous successful sum and asking to repeat input again.
    Function will over only by command "Stop"
    :param previous_sum: integers, floats or "Stop" command
    :return: float
    """
    output_sum = 0
    user_input = input("Enter series of integer or float numbers, divided by gap."
                       " Command stop, will over program: ").split(" ")
    try:
        for i in user_input:
            if i.lower() == "stop":
                return output_sum
            else:
                output_sum += float(i)
        # if user didn't stop computing recursion is calling
        print("-" * 100)
        print(f"Your current sum of numbers equals to {output_sum + previous_sum}.")
        return output_sum + sum_of_numbers(output_sum + previous_sum)


    except ValueError as error:
        print(f"Can't convert one of your input numbers, {error}\n"
              f"Your current sum of numbers computed before error input equals to {previous_sum}.")
        return sum_of_numbers(previous_sum)
