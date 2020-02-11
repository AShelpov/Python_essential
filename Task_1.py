"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""


import time
from collections import namedtuple
from itertools import cycle

LightTime = namedtuple("LightTime", "light running_time")


class TrafficLightModeError(Exception):
    pass

class TrafficLight():
    LIGHT_TIME = (LightTime("Red", 7), LightTime("Yellow", 2),  LightTime("Green", 10))


    def __init__(self):
        self.__light_time = TrafficLight.LIGHT_TIME
        self.__previous_mode = "Green"

    def running(self):
        for switch_mode in cycle(self.__light_time):
            self.checking_modes(switch_mode.light)
            print(switch_mode.light)
            start = time.time()
            while time.time() - start < switch_mode.running_time:
                pass
            self.__previous_mode = switch_mode.light

    class ModeError(Exception):
        pass

    def checking_modes(self, current_light):
        supposed_mode = ("Red", "Yellow", "Green")
        current_light_index = supposed_mode.index(current_light)
        previous_light = supposed_mode[current_light_index - 1]
        if previous_light == self.__previous_mode:
            pass
        else:
            raise TrafficLightModeError




a = TrafficLight()
a.running()