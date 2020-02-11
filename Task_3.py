"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (g et_full_name) и
дохода с учетом премии (g et_total_income) . Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""
import random as rnd

class Worker():
    def __init__(self, name:str, surname:str, position:str, income:float):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position
        wage_rate = rnd.random()
        income = float(income)
        self._income = {"wage": round(wage_rate * income, 2), "bonus": round((1 - wage_rate) * income, 2)}

class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        total_income = round(self._income["wage"] + self._income["bonus"], 2)
        return f"Total income of {self.get_full_name()} equals: {total_income}"


names = {"Kierra": "She", "Beckett": "She", "Celeste": "She", "Patricia": "She", "Ariel": "She", "James": "He",
         "Sarai": "He", "Maeve": "He", "Cassie": "She", "Leia": "She", "Steven": "He", "Elise": "She"}
surnames = ["Adams", "Hicks", "Mcdaniel", "Pruitt", "Conrad", "Gregory", "Berry",
            "Hernandez", "Richardson", "Gibson", "Randolph", "Serrano"]

positions = ["junior", "senior", "manager", "director", "CEO", "CFO"]

dict_of_workers = {}
for worker in ["worker_"+str(i + 1) for i in range(10)]:
    dict_of_workers[worker] = Position(rnd.choice(list(names.keys())), rnd.choice(surnames),
                                       rnd.choice(positions), rnd.uniform(50000, 100000))

for key, value in dict_of_workers.items():
    print(f"{key} is {value.get_full_name()}")
    print(f"{names[value.name]} is {value.position}")
    print(value.get_total_income())
    print("-"*100)