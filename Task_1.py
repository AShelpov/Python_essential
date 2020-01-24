"""Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

list_of_types = [777, 3454.3456, "this is string", [i for i in range(10,100,15)],
                 tuple(i for i in range(5)),  "this is bytes".encode("utf-8"), bytearray(b"byte_array"),
                 {"a": 100, "b": 200, "c": 300}]

for i in list_of_types:
    print(type(i))