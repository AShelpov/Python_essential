def my_function(a=0.0, b=1.0):
    """
    Divides 'a' by 'b' and return result.
    If one of input is string return error. Have positional arguments by default which calculation leads to zero
    :param a: float
    :param b: float
    :return: float
    """
    try:
        float(a)
        float(b)
    except ValueError as error:
        print(f"Error in input value of positional arguments. {error}.")
    else:
        try:
            result = a / b
        except ZeroDivisionError as error:
            print(f"Can not divide by zero.")
        else:
            return result

my_function()