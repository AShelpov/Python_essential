"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма) . Это могут быть обычные числа: V и
H , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
"""

from abc import ABC, abstractmethod


class AbstractClassDress:
    @abstractmethod
    def __init__(self, s, h):
        pass

    @abstractmethod
    def tissue_consumption(self):
        pass


class Dress(AbstractClassDress):

    def __init__(self, h=None, s=None):
        if (h is None) and (s is None):
            print(f"One of two dimensions must have a number. Got none")
        elif h is not None:
            try:
                self.__h = float(h)
                self.__type = "Suit"
            except ValueError:
                print("h parameter of height must be float")
        elif s is not None:
            try:
                self.__s = int(s)
                self.__type = "Coat"
            except ValueError:
                print(f"s parameter of size must be integer")
        else:
            print(f"Only one dimension must have number. Got two")

    @property
    def dimesion(self):
        if self.__type == "Suit":
            return f"Height is {self.__h}"
        else:
            return f"Size is {self.__s}"

    @property
    def type(self):
        return self.__type

    def tissue_consumption(self):
        if self.__type == "Suit":
            output = 2 * self.__h + 0.3
            return f"Tissue consumption for suit with height {self.__h} equals to {round(output, 2)} sq.sm."
        else:
            output =  self.__s / 6.5 + 0.5
            return f"Tissue consumption for coat with size {self.__s} equals to {round(output, 2)} sq.m."

    def __str__(self):
        return f"Type of dress is {self.__type} " \
            f"with dimension {'height' if self.__type == 'Suit' else 'size'} " \
            f"equals {self.__h if self.__type == 'Suit' else self.__s}."

a = Dress(182)
b = Dress(s=48)

print(a.dimesion)
print(a.type)
print(a.tissue_consumption())
print(a)

print("-"*100)

print(b.dimesion)
print(b.type)
print(b.tissue_consumption())
print(b)

print("-"*100)

c = Dress()
d = Dress(h=123, s=56)
e = Dress(h="asdfsg")
f = Dress(s="dfgh")
