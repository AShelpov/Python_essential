"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class InappropriateInput(Exception):
    def __init__(self, message=None):
        if message is None:
            self.message = "Inappropriate input"
        else:
            self.message = message


class MyData:
    def __init__(self):
        user_date = input("Enter your data as string with format 'day-month-year': ").split("-")
        if len(user_date) != 3:
            raise InappropriateInput("Can't convert your string to date. Wrong format of input.")
        else:
            self.day = MyData.convert_to_int(user_date[0])
            self.month = MyData.convert_to_int(user_date[1])
            self.year = MyData.convert_to_int(user_date[2])

    @classmethod
    def convert_to_int(cls, param):
        try:
            param = int(param)
            return param
        except ValueError:
            raise InappropriateInput(f"Can't convert '{param}' to integer.")

    @staticmethod
    def checking_date(day: int, month: int, year: int):
        """
        only raise exception if inappropriate number
        """
        if MyData.define_leap_year(year):
            year_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        else:
            year_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if year_dict.get(month) is None:
            raise InappropriateInput(f"Month number '{month}' out of range. Inappropriate input.")
        elif day not in [i for i in range(1, year_dict.get(month) + 1)]:
            raise InappropriateInput(f"Day must be in range from '1' to '{year_dict.get(month)}',"
                                     f" you enter '{day}'")
        elif (year < 0) or (year > 3000):
            raise InappropriateInput(f"Year must bi in range from '0' to '3000', you enter {year}")

    @classmethod
    def define_leap_year(cls, year: int):
        """
        return True if year is a leap
        """
        if year % 4 == 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False


a = MyData()
MyData.checking_date(a.day, a.month, a.year)
print()

