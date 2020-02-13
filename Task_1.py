"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__() ), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, i=0, j=0, filling=[]):
        if i == 0:
            self.__i = self.__determine_rows()
        else:
            self.__i = i

        if j == 0:
            self.__j = self.__determine_columns()
        else:
            self.__j = j

        if len(filling) == 0:
            self.__filling = self.__fill_matrix()
        else:
            self.__filling = filling
        print("="*100)
        print(f"Matrix {self.__i}X{self.__j} has been created")

    def __determine_rows(self):
        print("-"*100)
        print("Start to creating new matrix")
        number_of_rows = 0
        while True:
            try:
                number_of_rows = int(input("Enter number of rows. Must be integer: "))
                if number_of_rows <= 0:
                    print("Number of rows must be more than zero. Try again")
                    print("-"*100)
                    continue
                break
            except ValueError:
                print("You entered unappropriated data. Try again")
                print("-" * 100)
                continue
        return number_of_rows

    def __determine_columns(self):
        number_of_columns = 0
        while True:
            try:
                number_of_columns = int(input("Enter number of columns. Must be integer: "))
                if number_of_columns <= 0:
                    print("Number of columns must be more than zero. Try again")
                    print("-" * 100)
                    continue
                break
            except ValueError:
                print("You entered unappropriated data. Try again")
                print("-" * 100)
                continue

        return number_of_columns


    def __fill_matrix(self):
        count_of_rows =0
        output_list = []
        while count_of_rows != self.__i:
            try:
                row = [float(num) for num in
                       input(f"Enter number for row {count_of_rows + 1} divided by comma."
                             f" Must be integer or float: ").replace(" ", "").split(",")]
                if len(row) != self.__j:
                    print(f"Number of digits in row must be equals to {self.__j}, you entered {len(row)}. Try again.")
                    print("-"*100)
                    continue
                output_list.append(row)
                count_of_rows += 1
            except ValueError:
                print("Can't convert one of entered value. Try again")
                print("-"*100)
                continue
        return output_list

    def __str__(self):
        output = str()
        for row in range(self.__i):
            represent_row = f"{self.__filling[row]}\n"
            output += represent_row
        return output

    def __add__(self, other):
        if (self.__i != other.__i) or (self.__j != other.__j):
            print(f"Can't fold matrix with different shape. "
                  f"Shape of first matrix equals to {self.shape}, of second - {other.shape}.")
        else:
            output = []
            for row in range(self.__i):
                line = []
                for el in range(self.__j):
                    element = self.__filling[row][el] + other.__filling[row][el]
                    line.append(element)
                output.append(line)
            return Matrix(self.__i, self.__j, output)

    @property
    def shape(self):
        return f"({self.__i}x{self.__j})"

a = Matrix()
print(a)
print(a.shape)

b = Matrix(2, 2, [[10, 10], [10, 10]])
print(b)
print(b.shape)

c = a + b
print(c)
print(c.shape)