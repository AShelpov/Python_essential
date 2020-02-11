"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних
классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""
import random as rnd


class CarClassificationError(Exception):
    pass


class Car:
    def __init__(self, speed: float, color: str, name: str):
        self._speed = float(speed)
        self._color = color
        self._name = name
        self._is_police = False

    def go(self):
        return f"{self._color} {self._name} start moving with {self._speed} speed"

    def stop(self):
        self._speed = 0
        return f"{self._color} {self._name} has stopped"

    def turn(self, direction: str):
        if direction.lower() in ("right", "left", "backward"):
            return f"{self._color} {self._name} has turned " \
                f"{'to the' if direction.lower() in ('right', 'left') else ''} {direction.lower()}"
        else:
            raise CarClassificationError

    def show_speed(self):
        return f"Current speed of {self._color} {self._name} equals {self._speed} km/h"

    def interact_with_other(self, other):
        return f"No interaction between {self._color} {self._name} and {other._color} {other._name}"


class TownCar(Car):
    __max_speed = 60

    def show_speed(self):
        if self._speed > TownCar.__max_speed:
            return f"{self._color} {self._name} is over speed on {self._speed - TownCar.__max_speed} km/h"
        else:
            return super().show_speed()

    def go(self):
        if self._speed == 0:
            self._speed = round(rnd.uniform(30, 200), 2)
            return f"{self._color} {self._name} start moving" \
                f" with {TownCar.__max_speed if self._speed == 0 else self._speed} km/h speed"
        else:
            return f"{self._color} {self._name} is moving" \
                f" with {TownCar.__max_speed if self._speed == 0 else self._speed} km/h speed"

    def interact_with_other(self, other):
        self.__fine_counts = 0
        if self.__fine_counts == 3:
            return f"Driver of {self._color} {self._name} have been arrested for multiple overspeeding"
        if other._is_police and self._speed > TownCar.__max_speed:
            self.__fine_counts += 1
            self._speed = 0
            self.go()
            return f"OVERSPEEDING IS PROHIBITED GET YOUR {self.__fine_counts} FINE. " \
                f"YOU WILL BE ARRESTED AFTER THIRD FINE !!!"
        else:
            return f"Respect from the police. You are an careful driver"


class SportCar(Car):
    __max_speed = 110

    def show_speed(self):
        if self._speed > SportCar.__max_speed:
            return f"{self._color} {self._name} is over speed on {self._speed - SportCar.__max_speed} km/h"
        else:
            return super().show_speed()

    def go(self):
        if self._speed == 0:
            self._speed = round(rnd.uniform(30, 200), 2)
            return f"{self._color} {self._name} start moving" \
                f" with {SportCar.__max_speed if self._speed == 0 else self._speed} km/h speed"
        else:
            return f"{self._color} {self._name} is moving" \
                f" with {SportCar.__max_speed if self._speed == 0 else self._speed} km/h speed"

    def interact_with_other(self, other):
        self.__fine_counts = 0
        if self.__fine_counts == 3:
            return f"Driver of {self._color} {self._name} have been arrested for multiple overspeeding"
        if other._is_police and self._speed > SportCar.__max_speed:
            self.__fine_counts += 1
            self._speed = 0
            self.go()
            return f"OVERSPEEDING IS PROHIBITED GET YOUR {self.__fine_counts} FINE. " \
                f"YOU WILL BE ARRESTED AFTER THIRD FINE !!!"
        else:
            return f"Respect from the police. You are an careful driver"


class WorkCar(Car):
    __max_speed = 40

    def show_speed(self):
        if self._speed > WorkCar.__max_speed:
            return f"{self._color} {self._name} is over speed on {self._speed - WorkCar.__max_speed} km/h"
        else:
            return super().show_speed()

    def go(self):
        if self._speed == 0:
            self._speed = round(rnd.uniform(30, 200), 2)
            return f"{self._color} {self._name} start moving" \
                f" with {WorkCar.__max_speed if self._speed == 0 else self._speed} km/h speed"
        else:
            return f"{self._color} {self._name} is moving" \
                f" with {WorkCar.__max_speed if self._speed == 0 else self._speed} km/h speed"

    def interact_with_other(self, other):
        self.__fine_counts = 0
        if self.__fine_counts == 3:
            return f"Driver of {self._color} {self._name} have been arrested for multiple overspeeding"
        if other._is_police and self._speed > WorkCar.__max_speed:
            self.__fine_counts += 1
            self._speed = 0
            self.go()
            return f"OVERSPEEDING IS PROHIBITED GET YOUR {self.__fine_counts} FINE. " \
                f"YOU WILL BE ARRESTED AFTER THIRD FINE !!!"
        else:
            return f"Respect from the police. You are an careful driver"


class PoliceCar(Car):

    def __init__(self, speed: float, color: str, name: str):
        self._speed = float(speed)
        self._color = color.capitalize()
        self._name = name.capitalize()
        self._is_police = True

    def interact_with_other(self, other):
        other_car_class = other.__class__.__name__
        if other_car_class == "PoliceCar":
            return f"Hi, colleague"
        elif other_car_class == "TownCar" and other._speed > TownCar._TownCar__max_speed:
            self._speed = other._speed
            return f"STOP SUN OF A BITCH AND GET YOUR FINE."
        elif other_car_class == "SportCar" and other._speed > SportCar._SportCar__max_speed:
            self._speed = other._speed
            return f"STOP SUN OF A BITCH AND GET YOUR FINE."
        elif other_car_class == "WorkCar" and other._speed > WorkCar._WorkCar__max_speed:
            self._speed = other._speed
            return f"STOP SUN OF A BITCH AND GET YOUR FINE."
        else:
            return f"Respect from the police to driver of {other._color} {other._name}, hi is careful"

    def go(self):
        return f"Police {self._color} {self._name} start moving with {self._speed} speed"

    def stop(self):
        self._speed = 0
        return f"Police {self._color} {self._name} has stopped"

    def turn(self, direction: str):
        if direction.lower() in ("right", "left", "backward"):
            return f"Police {self._color} {self._name} has turned " \
                f"{'to the' if direction.lower() in ('right', 'left') else ''} {direction.lower()}"
        else:
            raise CarClassificationError

    def show_speed(self):
        return f"Current speed of police {self._color} {self._name} equals {self._speed} km/h"


colors = ["Black", "White", "Silver", "Green", "Yellow", "Brown", "Blue"]
names = ["Ford", "Oldsmobile", "GM", "Tesla", "Ferrari", "Lada", "Kamaz", "Uaz"]

dict_of_cars = {}
for i in range(10):
    var_name = "car_" + str(i + 1)
    car_name = rnd.choice(names)
    car_color = rnd.choice(colors)
    initial_speed = round(rnd.uniform(30, 200), 2)
    car_class = rnd.choice((TownCar, SportCar, WorkCar, PoliceCar))
    dict_of_cars[var_name] = car_class(initial_speed, car_color, car_name)


print(dict_of_cars["car_1"].turn("left"))
print(dict_of_cars["car_2"].turn("right"))
print(dict_of_cars["car_3"].stop())
print(dict_of_cars["car_6"].go())
print(dict_of_cars["car_8"].interact_with_other(dict_of_cars["car_10"]))
print(dict_of_cars["car_7"].show_speed())
print(dict_of_cars["car_1"].interact_with_other(dict_of_cars["car_1"]))
print(dict_of_cars["car_3"].interact_with_other(dict_of_cars["car_4"]))
print(dict_of_cars["car_6"].interact_with_other(dict_of_cars["car_6"]))
print(dict_of_cars["car_7"].interact_with_other(dict_of_cars["car_8"]))
print(dict_of_cars["car_8"].interact_with_other(dict_of_cars["car_9"]))
print(dict_of_cars["car_10"].interact_with_other(dict_of_cars["car_3"]))
print(dict_of_cars["car_5"].interact_with_other(dict_of_cars["car_4"]))
print(dict_of_cars["car_5"].go())
print(dict_of_cars["car_5"].interact_with_other(dict_of_cars["car_4"]))
print(dict_of_cars["car_4"].interact_with_other(dict_of_cars["car_9"]))






