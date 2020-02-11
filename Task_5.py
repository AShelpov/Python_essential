"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""

class Stationery():

    def __init__(self):
        self.title = "instance of Stationery"

    def draw(self):
        return f"Start drawing instance of the Stationery"


class Pen(Stationery):

    def __init__(self):
        self.title = "Pen"

    def draw(self):
        return f"I'm drawing a {self.title}"


class Pencil(Stationery):

    def __init__(self):
        self.title = "Pencil"

    def draw(self):
        return f"I'm drawing a {self.title}"


class Handle(Stationery):

    def __init__(self):
        self.title = "Handle"

    def draw(self):
        return f"I'm drawing a {self.title}"


a, b, c, d = Stationery(), Pen(), Pencil(), Handle()
print(a.draw())
print(b.draw())
print(c.draw())
print(d.draw())
