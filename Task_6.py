"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию int_func() .
"""

def int_func(input_text:str):
    """
    Shift first symbol in entered text into uppercase. If first symbol is digit or input text consist only from one gap
    or first symbol in entered text is gap, will return input text without any changes
    :param input_text: str
    :return: str
    """
    if input_text == "":
        return " "
    # for just one gap input
    elif input_text[0].isdigit() or input_text[0] == " ":
        return input_text
    else:
        output_text = input_text.capitalize()
        return output_text


def other_int_func(input_string:str):
    list_of_words = [i for i in input_string.split(" ")]
    output_string = str()
    for i in list_of_words:
        output_string += int_func(i)
        output_string += " "
    return output_string
