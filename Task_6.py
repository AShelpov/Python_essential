"""
Реализовать структуру данных « Товары ». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами (характеристиками товара: название,
цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
"""

list_of_goods = []

while True:
    print()
    list_of_names = []
    item_name = input("Enter name of item.\nIf you want stop the program and"
                      " print final catalog enter 'Stop': ")
    if item_name.lower() == "stop":
        break

    if len(list_of_goods) == 0:
        new_item = {"Name": item_name}
    else:
        for i in list_of_goods:
            list_of_names.append(i["Name"])
    if item_name in list_of_names:
        print()
        print("Item with such name is already exist. Choose another name")
        print("="*100)
        continue
    else:
        new_item = {"Name": item_name}
        item_price = input(f"Enter price of item - '{item_name}': ")
        item_unit_measure = input(f"Enter unit measure of item - '{item_name}': ")
        item_quantity = input(f"Enter quantity of item - '{item_name}' in {item_unit_measure}: ")
        new_item.update({"Price": item_price, "Unit measure": item_unit_measure, "Quantity": item_quantity})
        list_of_goods.append(new_item)


final_data_frame = enumerate(list_of_goods)
for i, item in final_data_frame:
    print(i + 1, item)

final_dictionary = {"Name": [], "Price": [], "Unit measure": [], "Quantity": []}
for i in list_of_goods:
    final_dictionary["Name"].append(i["Name"])
    final_dictionary["Price"].append(i["Price"])
    final_dictionary["Unit measure"].append(i["Unit measure"])
    final_dictionary["Quantity"].append(i["Quantity"])

print()
for key, values in final_dictionary.items():
    print(f"'{key}' : {values}")

