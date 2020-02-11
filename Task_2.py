"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road():

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def calculate_asphalt_mass(self, mass_per_1sq_meter, thickness_of_road):
        return self._length * self._width * mass_per_1sq_meter * thickness_of_road


a = Road(5000, 20)
output = a.calculate_asphalt_mass(25,5)


print(output)

