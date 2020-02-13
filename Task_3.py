"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение ( _add__() ), вычитание (_ _sub__()) ,
умножение (_ _mul__()) , деление (_ _truediv__()) . Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****. .., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n** .
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n***** .
"""


class Cell:
    def __init__(self, nucleuses=0):
        try:
            self.__nucleuses = int(nucleuses)
            if self.__nucleuses <= 0:
                print("Can create instance CellClass only with param of nucleuses more than 0")
        except ValueError:
            print("Can create instance CellClass only with integer param of nucleuses")

    @property
    def nucleuses(self):
        return self.__nucleuses

    def __str__(self):
        return f"Cell of CellClass with param nucleuses {self.__nucleuses}"

    def __add__(self, other):
        if other.__class__.__name__ == "Cell":
            output =  self.__nucleuses + other.__nucleuses
            self.__nucleuses = output
        else:
            print(f"Can sum only CellClass. You try to sum CellClass and {other.__class__.__name__}")

    def __sub__(self, other):
        if other.__class__.__name__ == "Cell":
            if (self.__nucleuses - other.__nucleuses) > 0:
                self.__nucleuses = self.__nucleuses - other.__nucleuses
            else:
                print(f"Difference between nucleuses in two cells less or equal zero")
        else:
            print(f"Can deduct only CellClass. You try to sum CellClass and {other.__class__.__name__}")

    def __mul__(self, other):
        if other.__class__.__name__ == "Cell":
            return Cell(self.__nucleuses * other.__nucleuses)
        else:
            print(f"Can multiply only CellClass. You try to sum CellClass and {other.__class__.__name__}")

    def __truediv__(self, other):
        if other.__class__.__name__ == "Cell":
            if (self.__nucleuses // other.__nucleuses) == 0:
                print(f"Division produce cell with param nucleuses zero")
            else:
                return Cell(self.__nucleuses // other.__nucleuses)
        else:
            print(f"Can divide only CellClass. You try to sum CellClass and {other.__class__.__name__}")

    def make_order(self, order):
        if (self.__nucleuses // order) == 0:
            return f"{'*' * self.__nucleuses}."
        else:
            output = str()
            for row in range((self.__nucleuses // order)):
                output += f"{'*' * order}\n"
            output += f"{'*' * (self.__nucleuses % order)}."
            return output

a = Cell(2)
b = Cell(-12)
c = Cell()
print(a.nucleuses)
print(a)
print("-"*100)

b = Cell(3)
print(b.nucleuses)
print(b)
print("-"*100)

c = a + b
print(a)
print("-"*100)

a = Cell(2)
d = a - b
print("-"*100)

e = a * b
print(e)
print("-"*100)

f = a / b
print("-"*100)

z = a + 12

x = Cell(23)
print(x.make_order(5))
print()

print(x.make_order(7))
print()

print(x.make_order(11))
print()

print(x.make_order(20))
print()

print(x.make_order(26))
print()




